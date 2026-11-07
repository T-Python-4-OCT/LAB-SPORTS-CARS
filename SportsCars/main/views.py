from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404


# All the cars of the website (prices are starting prices in Saudi Arabia)
cars = [
    {
        "slug": "k8",
        "name": "Kia K8",
        "type": "Premium Sedan",
        "price": "158,607",
        "engine": "3.5L V6",
        "power": "297 hp",
        "body": "Sedan",
        "seats": "5 Seats",
        "image": "images/cars/k8-front.jpg",
        "has_details": True,
        "gallery": [
            "images/cars/k8-front.jpg",
            "images/cars/k8-back.jpg",
            "images/cars/k8-front-inside.jpg",
            "images/cars/k8-back-inside.jpg",
        ],
        "title": "The Flagship, Redefined",
        "description": "The Kia K8 is a premium sedan with a bold design, a wide and quiet cabin, and a strong V6 engine. It brings luxury and comfort to every drive.",
    },
    {
        "slug": "k5",
        "name": "Kia K5",
        "type": "Sport Sedan",
        "price": "147,163",
        "engine": "2.5L GDi",
        "power": "191 hp",
        "body": "Sedan",
        "seats": "5 Seats",
        "image": "images/cars/k5-front.jpg",
        "has_details": True,
        "gallery": [
            "images/cars/k5-front.jpg",
            "images/cars/k5-back.jpg",
            "images/cars/k5-front-inside.jpg",
        ],
        "title": "Bold Design, Sporty Soul",
        "description": "The Kia K5 is a sporty sedan with a fastback shape and smart technology. It is made for drivers who want style and performance together.",
    },
    {
        "slug": "k4",
        "name": "Kia K4",
        "type": "Compact Sedan",
        "price": "84,999",
        "engine": "1.6L",
        "power": "121 hp",
        "body": "Sedan",
        "seats": "5 Seats",
        "image": "images/cars/k4-front.jpg",
        "has_details": True,
        "gallery": [
            "images/cars/k4-front.jpg",
            "images/cars/k4-back.jpg",
            "images/cars/k4-front-inside.jpg",
            "images/cars/k4-back-inside.jpg",
        ],
        "title": "A New Era of Compact",
        "description": "The Kia K4 is the new compact sedan with a futuristic look, wide screens inside, and modern safety features for everyday driving.",
    },
    {
        "slug": "k3",
        "name": "Kia K3",
        "type": "Compact Sedan",
        "price": "71,478",
        "engine": "1.6L",
        "power": "123 hp",
        "body": "Sedan",
        "seats": "5 Seats",
        "image": "images/cars/k3-front.jpg",
        "has_details": False,
        "title": "Smart Choice, Every Day",
        "description": "The Kia K3 is a practical and efficient sedan. It is easy to drive in the city and comfortable on long trips.",
    },
    {
        "slug": "pegas",
        "name": "Kia Pegas",
        "type": "City Sedan",
        "price": "55,053",
        "engine": "1.4L MPI",
        "power": "93 hp",
        "body": "Sedan",
        "seats": "5 Seats",
        "image": "images/cars/pegas-front.jpg",
        "has_details": False,
        "title": "Small Car, Big Value",
        "description": "The Kia Pegas is a light and economical city car. It saves fuel and gives you good space for its size.",
    },
    {
        "slug": "sorento",
        "name": "Kia Sorento",
        "type": "Family SUV",
        "price": "142,137",
        "engine": "3.5L V6",
        "power": "268 hp",
        "body": "SUV",
        "seats": "7 Seats",
        "image": "images/cars/sorento-front.jpg",
        "has_details": False,
        "title": "Room for Every Adventure",
        "description": "The Kia Sorento is a 7-seat SUV with a strong V6 engine, a premium cabin and space for the whole family.",
    },
]


# Create your views here.

def home_view(request: HttpRequest):
    # show the first 3 cars on the home page
    featured_cars = cars[:3]
    return render(request, "main/home.html", {"featured_cars": featured_cars})


def cars_view(request: HttpRequest):
    return render(request, "main/cars.html", {"cars": cars})


def car_detail_view(request: HttpRequest, slug: str):
    # find the car that has this slug (only cars with details have a page)
    for car in cars:
        if car["slug"] == slug and car["has_details"]:
            return render(request, "main/car_detail.html", {"car": car})

    raise Http404("Car not found")


def about_view(request: HttpRequest):
    return render(request, "main/about.html")


def theme_view(request: HttpRequest, mode: str):
    # go back to the same page the user was on
    next_page = request.GET.get("next", "/")
    if not next_page.startswith("/") or next_page.startswith("//"):
        next_page = "/"

    response = redirect(next_page)

    # save the theme in a cookie for one year
    if mode in ["light", "dark"]:
        response.set_cookie("theme", mode, max_age=60*60*24*365)

    return response
