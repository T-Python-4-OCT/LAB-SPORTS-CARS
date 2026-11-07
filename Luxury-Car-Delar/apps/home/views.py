from django.shortcuts import render

from apps.data import CARS


def home(request):
    featured_cars = [
        {"slug": slug, **car}
        for slug, car in CARS.items()
        if car["featured"]
    ]

    context = {
        "featured_cars": featured_cars,
    }

    return render(request, "home/index.html", context)