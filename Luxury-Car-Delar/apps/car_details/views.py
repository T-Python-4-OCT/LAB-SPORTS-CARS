from django.http import Http404
from django.shortcuts import render

from apps.data import CARS


def car_detail(request, slug):
    car = CARS.get(slug)

    if car is None:
        raise Http404("Car not found")

    context = {
        "car": car,
        "slug": slug,
    }

    return render(request, "car_details/detail.html", context)