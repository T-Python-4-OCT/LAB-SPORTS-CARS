
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import (
    Q,
    F,
    Case,
    When,
    Value,
    FloatField,
)
from django.db.models.functions import Cast, Replace
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

from .forms import CarInquiryForm
from .models import Car


# ==========================================
# HOME
# ==========================================

def home(request):
    featured_cars = Car.objects.filter(
        is_featured=True
    )

    return render(
        request,
        "cars/home.html",
        {
            "featured_cars": featured_cars,
        },
    )


# ==========================================
# ALL CARS - SEARCH & FILTER
# ==========================================

def all_cars(request):
    cars = Car.objects.all()

    search_query = request.GET.get(
        "search", ""
    ).strip()

    selected_brand = request.GET.get(
        "brand", ""
    ).strip()

    selected_power = request.GET.get(
        "power", ""
    ).strip()

    selected_price = request.GET.get(
        "max_price", ""
    ).strip()

    selected_year = request.GET.get(
        "min_year", ""
    ).strip()

    selected_sort = request.GET.get(
        "sort", "default"
    ).strip()

    brands = (
        Car.objects
        .order_by("brand")
        .values_list("brand", flat=True)
        .distinct()
    )

    # Search
    if search_query:
        cars = cars.filter(
            Q(name__icontains=search_query)
            | Q(brand__icontains=search_query)
            | Q(engine__icontains=search_query)
        )

    # Brand filter
    if selected_brand:
        cars = cars.filter(
            brand=selected_brand
        )

    # Horsepower filter
    power_options = {
        "500": 500,
        "1000": 1000,
    }

    if selected_power in power_options:
        cars = cars.filter(
            horsepower__gte=power_options[selected_power]
        )
    else:
        selected_power = ""

    # Model year filter
    year_options = {
        "2020": 2020,
        "2024": 2024,
        "2025": 2025,
    }

    if selected_year in year_options:
        cars = cars.filter(
            year__gte=year_options[selected_year]
        )
    else:
        selected_year = ""

    # Convert stored numeric prices for filtering.
    # Existing price field is a CharField.
    cleaned_price = Replace(
        "price",
        Value(","),
        Value("")
    )

    cars = cars.annotate(
        price_number=Case(
            When(
                price__regex=r"^[0-9][0-9,]*(\.[0-9]+)?$",
                then=Cast(
                    cleaned_price,
                    FloatField()
                )
            ),
            default=Value(None),
            output_field=FloatField()
        )
    )

    price_options = {
        "1000000": 1000000,
        "3000000": 3000000,
        "8000000": 8000000,
    }

    if selected_price in price_options:
        cars = cars.filter(
            price_number__lte=price_options[selected_price]
        )
    else:
        selected_price = ""

    # Sort
    sort_options = {
        "default": ("id",),
        "name": ("name", "id"),
        "newest": ("-year", "id"),
        "oldest": ("year", "id"),
        "power_desc": ("-horsepower", "id"),
        "power_asc": ("horsepower", "id"),
    }

    valid_sorts = set(sort_options) | {
        "price_asc",
        "price_desc",
    }

    if selected_sort not in valid_sorts:
        selected_sort = "default"

    if selected_sort == "price_asc":
        cars = cars.order_by(
            F("price_number").asc(nulls_last=True),
            "id"
        )

    elif selected_sort == "price_desc":
        cars = cars.order_by(
            F("price_number").desc(nulls_last=True),
            "id"
        )

    else:
        cars = cars.order_by(
            *sort_options[selected_sort]
        )

    # Pagination
    paginator = Paginator(cars, 6)

    page_obj = paginator.get_page(
        request.GET.get("page", 1)
    )

    return render(
        request,
        "cars/all_cars.html",
        {
            "cars": page_obj,
            "page_obj": page_obj,
            "paginator": paginator,
            "cars_count": paginator.count,
            "brands": brands,
            "search_query": search_query,
            "selected_brand": selected_brand,
            "selected_power": selected_power,
            "selected_price": selected_price,
            "selected_year": selected_year,
            "selected_sort": selected_sort,
            "has_filters": bool(
                search_query
                or selected_brand
                or selected_power
                or selected_price
                or selected_year
            ),
        },
    )


# ==========================================
# WISHLIST
# ==========================================

def wishlist(request):
    raw_ids = request.GET.getlist("cars")
    car_ids = []

    for raw_id in raw_ids:
        if not raw_id.isdigit():
            continue

        car_id = int(raw_id)

        if car_id > 0 and car_id not in car_ids:
            car_ids.append(car_id)

        if len(car_ids) >= 100:
            break

    cars_by_id = Car.objects.in_bulk(car_ids)

    saved_cars = [
        cars_by_id[car_id]
        for car_id in car_ids
        if car_id in cars_by_id
    ]

    return render(
        request,
        "cars/wishlist.html",
        {
            "cars": saved_cars,
            "cars_count": len(saved_cars),
        },
    )


# ==========================================
# COMPARE CARS
# ==========================================

def compare_cars(request):
    selected_ids = request.GET.getlist("cars")
    unique_ids = list(dict.fromkeys(selected_ids))

    error = None
    selected_cars = []

    if len(unique_ids) < 2:
        error = "Please select at least 2 cars to compare."

    elif len(unique_ids) > 3:
        error = "You can compare a maximum of 3 cars."

    elif not all(
        car_id.isdigit()
        for car_id in unique_ids
    ):
        error = "Invalid car selection."

    else:
        car_ids = [
            int(car_id)
            for car_id in unique_ids
        ]

        cars_by_id = Car.objects.in_bulk(car_ids)

        if len(cars_by_id) != len(car_ids):
            error = (
                "One or more selected cars are unavailable."
            )

        else:
            selected_cars = [
                cars_by_id[car_id]
                for car_id in car_ids
            ]

    highest_horsepower = None
    newest_year = None

    if selected_cars:
        highest_horsepower = max(
            car.horsepower
            for car in selected_cars
        )

        newest_year = max(
            car.year
            for car in selected_cars
        )

    return render(
        request,
        "cars/compare.html",
        {
            "cars": selected_cars,
            "error": error,
            "highest_horsepower": highest_horsepower,
            "newest_year": newest_year,
        },
    )


# ==========================================
# CAR DETAILS + INQUIRY FORM
# ==========================================

def car_detail(request, car_id):
    car = get_object_or_404(
        Car,
        id=car_id
    )

    if request.method == "POST":
        form = CarInquiryForm(request.POST)

        if form.is_valid():
            inquiry = form.save(commit=False)

            # The car comes from the URL, not user input.
            inquiry.car = car
            inquiry.save()

            messages.success(
                request,
                "Your inquiry has been sent successfully!"
            )

            return redirect(
                "cars:car_detail",
                car_id=car.id
            )

    else:
        form = CarInquiryForm()

    return render(
        request,
        "cars/car_detail.html",
        {
            "car": car,
            "form": form,
        },
    )


# ==========================================
# ABOUT
# ==========================================

def about(request):
    return render(
        request,
        "cars/about.html"
    )
