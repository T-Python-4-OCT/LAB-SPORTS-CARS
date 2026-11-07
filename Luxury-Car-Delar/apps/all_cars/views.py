
from django.shortcuts import render

from apps.data import CARS


def all_cars(request):
    all_vehicles = [
        {"slug": slug, **car}
        for slug, car in CARS.items()
    ]

    selected = {
        key: request.GET.get(key, "").strip()
        for key in ("q", "brand", "model", "price", "year", "sort")
    }

    brands = sorted({car["brand"] for car in all_vehicles})
    models = sorted({car["model"] for car in all_vehicles})
    years = sorted(
        {car["year"] for car in all_vehicles},
        reverse=True
    )

    cars = all_vehicles

    # Search by name, brand, or model
    if selected["q"]:
        query = selected["q"].lower()

        cars = [
            car for car in cars
            if query in (
                f"{car['name']} {car['brand']} {car['model']}"
            ).lower()
        ]

    # Brand filter
    if selected["brand"]:
        cars = [
            car for car in cars
            if car["brand"] == selected["brand"]
        ]

    # Model filter
    if selected["model"]:
        cars = [
            car for car in cars
            if car["model"] == selected["model"]
        ]

    # Year filter
    if selected["year"]:
        cars = [
            car for car in cars
            if str(car["year"]) == selected["year"]
        ]

    # Price range filter
    if selected["price"] == "under":
        cars = [
            car for car in cars
            if car["price"] < 1200000
        ]

    elif selected["price"] == "middle":
        cars = [
            car for car in cars
            if 1200000 <= car["price"] <= 1500000
        ]

    elif selected["price"] == "above":
        cars = [
            car for car in cars
            if car["price"] > 1500000
        ]

    # Sorting
    if selected["sort"] == "price_asc":
        cars = sorted(cars, key=lambda car: car["price"])

    elif selected["sort"] == "price_desc":
        cars = sorted(
            cars,
            key=lambda car: car["price"],
            reverse=True
        )

    elif selected["sort"] == "newest":
        cars = sorted(
            cars,
            key=lambda car: car["year"],
            reverse=True
        )

    context = {
        "cars": cars,
        "car_count": len(cars),
        "brands": brands,
        "models": models,
        "years": years,
        "selected": selected,
    }

    return render(request, "all_cars/index.html", context)
