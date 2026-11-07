
from django.shortcuts import render
from cars.views import cars


def home(request):
    return render(request, "main/home.html", {"featured_cars": cars[:3]})


def about(request):
    return render(request, "main/about.html")
