from django.shortcuts import render
from django.http import HttpRequest, Http404
from .data import cars


def home_view(request: HttpRequest):
    return render(request, "main/home.html", {"cars": cars})


def cars_view(request: HttpRequest):
    return render(request, "main/cars.html", {"cars": cars})


def car_detail_view(request: HttpRequest, car_id):
    for car in cars:
        if car["id"] == car_id:
            return render(request, "main/car_detail.html", {"car": car})
    raise Http404("Car not found")


def about_view(request: HttpRequest):
    return render(request, "main/about.html")