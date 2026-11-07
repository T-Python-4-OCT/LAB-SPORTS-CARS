from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

from .data import CARS, CATEGORIES

app_name = "cars"

def home(request):
    return render(request, "home.html", {"featured": CARS[:3]})


def car_list(request):
    q = request.GET.get("q", "").strip().lower()
    cat = request.GET.get("category", "")
    cars = [
        c for c in CARS
        if (not cat or c["category"] == cat)
        and (not q or q in c["name"].lower())
    ]
    return render(request, "cars.html", {
        "cars": cars,
        "categories": CATEGORIES,
        "active_cat": cat,
        "q": request.GET.get("q", ""),
    })


def car_detail(request, slug):
    car = next((c for c in CARS if c["slug"] == slug), None)
    if car is None:
        raise Http404("Car not found")
    related = [c for c in CARS if c["slug"] != slug][:3]
    return render(request, "car_detail.html", {"car": car, "related": related})


def about(request):
    return render(request, "about.html")


def toggle_theme(request):
    current = request.COOKIES.get("theme", "light")
    new = "light" if current == "dark" else "dark"

    back = request.META.get("HTTP_REFERER", "")
    if not url_has_allowed_host_and_scheme(back, allowed_hosts={request.get_host()}):
        back = "/"

    response = redirect(back)
    response.set_cookie("theme", new, max_age=60 * 60 * 24 * 365)
    return response