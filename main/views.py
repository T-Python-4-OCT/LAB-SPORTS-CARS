from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from .cars_data import CARS, KEY_FEATURES, featured_cars, get_car

PRICE_RANGES = {
    "under-800k": ("Under SAR 800K", 0, 800_000),
    "800k-1200k": ("SAR 800K – 1.2M", 800_000, 1_200_000),
    "over-1200k": ("Over SAR 1.2M", 1_200_000, 10**12),
}


def home_view(request):
    return render(request, "main/home.html", {"featured_cars": featured_cars()})


def all_cars_view(request):
    # Filters come from the GET form on the page (no JavaScript needed)
    model = request.GET.get("model", "")
    price = request.GET.get("price", "")
    year = request.GET.get("year", "")

    cars = CARS
    if model:
        cars = [c for c in cars if c["slug"] == model]
    if price in PRICE_RANGES:
        _, low, high = PRICE_RANGES[price]
        cars = [c for c in cars if low <= c["price_value"] < high]
    if year.isdigit():
        cars = [c for c in cars if c["year"] == int(year)]

    return render(request, "main/all_cars.html", {
        "cars": cars,
        "all_cars": CARS,
        "years": sorted({c["year"] for c in CARS}, reverse=True),
        "price_ranges": [(key, label) for key, (label, _, _) in PRICE_RANGES.items()],
        "selected": {"model": model, "price": price, "year": year},
    })


def car_detail_view(request, slug):
    car = get_car(slug)
    if car is None:
        raise Http404("Car not found")

    # Prepare gallery slides with their previous / next index for the CSS slider
    total = len(car["gallery"])
    gallery = [
        {"image": img, "index": i, "prev": (i - 1) % total, "next": (i + 1) % total}
        for i, img in enumerate(car["gallery"])
    ]
    related = [c for c in featured_cars() if c["slug"] != slug]
    return render(request, "main/car_detail.html", {
        "car": car,
        "gallery": gallery,
        "key_features": KEY_FEATURES,
        "related": related,
    })


def about_view(request):
    return render(request, "main/about.html")


def toggle_theme_view(request):
    """Switch light/dark mode, remember it in a cookie, then go back to the same page."""
    next_url = request.GET.get("next", "/")
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = "/"
    new_theme = "light" if request.COOKIES.get("theme") == "dark" else "dark"
    response = redirect(next_url)
    response.set_cookie("theme", new_theme, max_age=60 * 60 * 24 * 365)
    return response
