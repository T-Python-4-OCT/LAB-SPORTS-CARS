
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import CarForm
from .models import Car


# ==========================================
# MANAGE CARS
# ==========================================

@staff_member_required(login_url="admin:login")
@permission_required(
    "cars.view_car",
    raise_exception=True
)
def manage_cars(request):

    search_query = request.GET.get(
        "search", ""
    ).strip()

    selected_featured = request.GET.get(
        "featured", "all"
    ).strip()

    cars = Car.objects.all()

    if search_query:
        cars = cars.filter(
            Q(name__icontains=search_query)
            | Q(brand__icontains=search_query)
            | Q(engine__icontains=search_query)
        )

    if selected_featured == "yes":
        cars = cars.filter(is_featured=True)

    elif selected_featured == "no":
        cars = cars.filter(is_featured=False)

    else:
        selected_featured = "all"

    cars = cars.order_by("-id")

    paginator = Paginator(cars, 8)

    page_obj = paginator.get_page(
        request.GET.get("page")
    )

    return render(
        request,
        "cars/manage_cars.html",
        {
            "cars": page_obj,
            "page_obj": page_obj,
            "search_query": search_query,
            "selected_featured": selected_featured,
            "cars_count": paginator.count,
            "total_cars": Car.objects.count(),
            "featured_count": Car.objects.filter(
                is_featured=True
            ).count(),
            "can_add": request.user.has_perm(
                "cars.add_car"
            ),
            "can_edit": request.user.has_perm(
                "cars.change_car"
            ),
        },
    )


# ==========================================
# ADD CAR
# ==========================================

@staff_member_required(login_url="admin:login")
@permission_required(
    "cars.add_car",
    raise_exception=True
)
def add_car(request):

    if request.method == "POST":
        form = CarForm(request.POST)

        if form.is_valid():
            car = form.save()

            messages.success(
                request,
                f"{car.name} has been added successfully."
            )

            return redirect("cars:manage_cars")

    else:
        form = CarForm()

    return render(
        request,
        "cars/car_form.html",
        {
            "form": form,
            "page_title": "ADD NEW",
            "page_highlight": "CAR.",
            "page_description": (
                "Add a new vehicle to your showroom."
            ),
            "submit_label": "CREATE CAR",
            "is_edit": False,
        },
    )


# ==========================================
# EDIT CAR
# ==========================================

@staff_member_required(login_url="admin:login")
@permission_required(
    "cars.change_car",
    raise_exception=True
)
def edit_car(request, car_id):

    car = get_object_or_404(
        Car,
        pk=car_id
    )

    if request.method == "POST":
        form = CarForm(
            request.POST,
            instance=car
        )

        if form.is_valid():
            updated_car = form.save()

            messages.success(
                request,
                f"{updated_car.name} has been updated successfully."
            )

            return redirect("cars:manage_cars")

    else:
        form = CarForm(instance=car)

    return render(
        request,
        "cars/car_form.html",
        {
            "form": form,
            "car": car,
            "page_title": "EDIT",
            "page_highlight": "CAR.",
            "page_description": (
                "Update vehicle information and settings."
            ),
            "submit_label": "SAVE CHANGES",
            "is_edit": True,
        },
    )
