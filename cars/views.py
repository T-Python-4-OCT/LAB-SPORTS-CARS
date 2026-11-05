from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest
from django.utils.http import url_has_allowed_host_and_scheme

CARS = [
    {'slug': 'genesis-gv80-coupe', 'name': 'Genesis GV80 Coupe', 'price': 329000, 'price_text': 'SAR 329,000', 'year': 2026, 'image': 'images/ferrari-card.jpg'},
    {'slug': 'genesis-g70', 'name': 'Genesis G70', 'price': 192435, 'price_text': 'SAR 192,435', 'year': 2026, 'image': 'images/porsche-card.jpg'},
    {'slug': 'genesis-g80', 'name': 'Genesis G80', 'price': 201500, 'price_text': 'SAR 201,500', 'year': 2026, 'image': 'images/genses-car3.jpg'},
]

PRICE_RANGES = {
    'under-200k': (0, 199999),
    '200k-300k': (200000, 300000),
    'over-300k': (300001, 10_000_000),
}


def home(request: HttpRequest):
    return render(request, 'home.html')


def all_cars(request: HttpRequest):
    q = request.GET.get('q', '').strip()
    model = request.GET.get('model', '')
    price = request.GET.get('price', '')
    year = request.GET.get('year', '')

    cars = CARS
    if q:
        cars = [car for car in cars if q.lower() in car['name'].lower()]
    if model:
        cars = [car for car in cars if car['slug'] == model]
    if price in PRICE_RANGES:
        low, high = PRICE_RANGES[price]
        cars = [car for car in cars if low <= car['price'] <= high]
    if year:
        cars = [car for car in cars if str(car['year']) == year]

    context = {
        'cars': cars,
        'all_models': CARS,
        'q': q,
        'model': model,
        'price': price,
        'year': year,
    }
    return render(request, 'all_cars.html', context)


def car_detail(request: HttpRequest, car_slug):
    return render(request, 'car_detail.html', {'car_slug': car_slug})


def about(request: HttpRequest):
    return render(request, 'about.html')


def set_theme(request: HttpRequest, theme):
    if theme not in ('light', 'dark'):
        theme = 'light'

    next_url = request.GET.get('next')
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = resolve_url('home')

    response = redirect(next_url)
    response.set_cookie('site_theme', theme, max_age=60 * 60 * 24 * 365)
    return response