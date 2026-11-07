from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from .data import CARS


def index(request):
    return render(request, 'main/index.html', {'cars': CARS})


def all_cars(request):
    categories = sorted({c['category'] for c in CARS})
    return render(request, 'main/cars.html', {'cars': CARS, 'categories': categories})


def car_detail(request, slug):
    car = next((c for c in CARS if c['slug'] == slug), None)
    if car is None:
        raise Http404('Car not found')
    others = [c for c in CARS if c['slug'] != slug]
    return render(request, 'main/car_detail.html', {'car': car, 'others': others})


def about(request):
    return render(request, 'main/about.html')


def body_dark(request):
    new = 'light' if request.COOKIES.get('theme') == 'dark' else 'dark'
    back = request.META.get('HTTP_REFERER', '/')
    if not url_has_allowed_host_and_scheme(back, allowed_hosts={request.get_host()}):
        back = '/'
    response = redirect(back)
    response.set_cookie('theme', new, max_age=60 * 60 * 24 * 365)
    return response