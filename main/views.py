from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
from .data import cars


def home_view(request: HttpRequest):
    return render(request, "main/home.html", {"cars": cars})


def cars_view(request: HttpRequest):
    brand = request.GET.get("brand")

    filtered_cars = []
    for car in cars:
        if not brand or car["brand"] == brand:
            filtered_cars.append(car)

    brands = []
    for car in cars:
        if car["brand"] not in brands:
            brands.append(car["brand"])

    return render(request, "main/cars.html", {
        "cars": filtered_cars,
        "brands": brands,
        "selected_brand": brand,
    })

def car_detail_view(request: HttpRequest, car_id):
    for car in cars:
        if car["id"] == car_id:
            return render(request, "main/car_detail.html", {"car": car})
    raise Http404("Car not found")


def about_view(request: HttpRequest):
    return render(request, "main/about.html")

def toggle_theme(request: HttpRequest):
    current = request.COOKIES.get("theme", "light")
    new_theme = "light" if current == "dark" else "dark"

    next_url = request.META.get("HTTP_REFERER") or "/"
    response = redirect(next_url)
    response.set_cookie("theme", new_theme, max_age=60 * 60 * 24 * 30)
    return response

def contact_view(request: HttpRequest):
    return render(request, "main/contact.html")