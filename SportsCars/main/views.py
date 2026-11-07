from django.shortcuts import render, redirect
from django.http import Http404
from .data import CARS


def get_price(car):
    return car["price"]


def get_cars(request):
    lang = request.COOKIES.get("lang", "en")

    cars = []
    for car in CARS:
        if lang == "ar":
            cars.append({**car, **car["ar"]})
        else:
            cars.append(car)
    return cars


def home_view(request):
    return render(request, "main/index.html", {"cars": get_cars(request)})


def cars_view(request):
    model = request.GET.get("model", "")
    price = request.GET.get("price", "")
    sort = request.GET.get("sort", "")

    all_cars = get_cars(request)

    cars = []
    for car in all_cars:
        if model and car["slug"] != model:
            continue
        if price == "under500" and car["price"] >= 500000:
            continue
        if price == "500to1m" and (car["price"] < 500000 or car["price"] > 1000000):
            continue
        if price == "over1m" and car["price"] <= 1000000:
            continue
        cars.append(car)

    if sort == "low":
        cars = sorted(cars, key=get_price)
    elif sort == "high":
        cars = sorted(cars, key=get_price, reverse=True)

    context = {
        "cars": cars,
        "all_cars": all_cars,
        "model": model,
        "price": price,
        "sort": sort,
    }
    return render(request, "main/cars.html", context)


def car_detail_view(request, slug):
    all_cars = get_cars(request)

    for car in all_cars:
        if car["slug"] == slug:
            others = []
            for other in all_cars:
                if other["slug"] != slug:
                    others.append(other)

            return render(request, "main/car_detail.html", {"car": car, "others": others})

    raise Http404("Car not found")


def about_view(request):
    return render(request, "main/about.html")


def mode_view(request, mode):
    if mode not in ("light", "dark"):
        mode = "light"

    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie("mode", mode, max_age=60 * 60 * 24 * 365)
    return response


def lang_view(request, lang):
    if lang not in ("en", "ar"):
        lang = "en"

    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365)
    return response
#mohammad Alnsafi