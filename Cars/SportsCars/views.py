from django.shortcuts import render, redirect
from django.http import HttpRequest

def home_page(request: HttpRequest):
 return render(request, "main/index.html")

def about_view(request):
    return render(request, "main/About.html")

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
            "image": "imgas/porsche.jpg",
            "url": "porsche"
        },
        {
            "name": "Ferrari F8",
            "brand": "ferrari",
            "price": 950000,
            "image": "imgas/ferrari.jpg",
            "url": "ferrari"
        },
        {
            "name": "Lamborghini Huracan",
            "brand": "lamborghini",
            "price": 850000,
            "image": "imgas/lamborghini.jpg",
            "url": "lamborghini"
        }
    ]

    return render(request, "main/AllCars.html", {"cars": cars})

def porsche_view(request):
    return render(request, "main/Porsche.html")


def ferrari_view(request):
    return render(request, "main/Ferrari.html")


def lamborghini_view(request):
    return render(request, "main/Lamborghini.html")

def contact_view(request):
    return render(request, "main/Contact.html")

