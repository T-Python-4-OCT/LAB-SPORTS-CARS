from django.shortcuts import render, redirect
from django.http import HttpRequest


def home_view(request: HttpRequest):
    return render(request, "main/home.html")


def all_cars_view(request: HttpRequest):
    return render(request, "main/all_cars.html")


def about_view(request: HttpRequest):
    return render(request, "main/about.html")


def range_rover_view(request: HttpRequest):
    car = {
        "name": "Range Rover",
        "slug": "range-rover",
        "price": "SAR 795,000",
        "engine": "4.4L Twin-Turbo V8",
        "power": "523 hp",
        "acceleration": "4.6 s",
        "top_speed": "250 km/h",
        "overview_title": "The Iconic Range Rover, Elevated",
        "overview_text": "A perfect balance of refined luxury and legendary capability.",
    }
    return render(request, "main/car_detail.html", {"car": car})


def defender_view(request: HttpRequest):
    car = {
        "name": "Defender",
        "slug": "defender",
        "price": "SAR 465,000",
        "engine": "3.0L Inline-6 Turbo",
        "power": "400 hp",
        "acceleration": "6.1 s",
        "top_speed": "191 km/h",
        "overview_title": "Built for Any Adventure",
        "overview_text": "Unstoppable capability with modern comfort, ready for any terrain.",
    }
    return render(request, "main/car_detail.html", {"car": car})


def discovery_view(request: HttpRequest):
    car = {
        "name": "Discovery",
        "slug": "discovery",
        "price": "SAR 325,000",
        "engine": "2.0L Turbo",
        "power": "249 hp",
        "acceleration": "7.5 s",
        "top_speed": "225 km/h",
        "overview_title": "Versatile by Design",
        "overview_text": "Flexible space and smart technology for every family journey.",
    }
    return render(request, "main/car_detail.html", {"car": car})

def toggle_theme_view(request: HttpRequest):
    current = request.COOKIES.get("theme", "light")
    new_theme = "dark" if current == "light" else "light"

    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie("theme", new_theme)
    return response