from django.shortcuts import render, redirect
from django.http import HttpRequest

def home_page(request: HttpRequest):
 return render(request, "main/index.html")

def trems_view(request: HttpRequest):
 return render(request, "main/Trems.html")

def dark_mode(request):
 current_mode = request.COOKIES.get("dark_mode", "light")

 new_mode = "light" if current_mode == "dark" else "dark"

 response = redirect(request.META.get("HTTP_REFERER", "/"))

 response.set_cookie(
    "dark_mode",new_mode,max_age=60 * 60 * 24 * 30
)

 return response

def all_cars(request):
    cars = [
        {
            "name": "Porsche 911",
            "brand": "porsche",
            "price": 450000,
            "image": "images/porsche.jpg",
            "url": "porsche"
        },
        {
            "name": "Ferrari F8",
            "brand": "ferrari",
            "price": 950000,
            "image": "images/ferrari.jpg",
            "url": "ferrari"
        },
        {
            "name": "Lamborghini Huracan",
            "brand": "lamborghini",
            "price": 850000,
            "image": "images/lamborghini.jpg",
            "url": "lamborghini"
        }
    ]

    return render(request, "main/AllCars.html", {"cars": cars})

