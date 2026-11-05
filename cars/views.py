from django.http import Http404
from django.shortcuts import render

from .data import CARS


def home(request):
    # أول 3 سيارات = الأكثر مبيعاً
    return render(request, 'cars/home.html', {'featured': CARS[:3]})


def car_list(request):
    # request.GET يقرأ ما بعد علامة ? في الرابط، مثل /cars/?category=SUV&sort=price_asc
    category = request.GET.get('category', '')
    sort = request.GET.get('sort', '')

    cars = CARS
    if category:
        cars = [c for c in cars if c['category'] == category]
    if sort == 'price_asc':
        cars = sorted(cars, key=lambda c: c['price'])
    elif sort == 'price_desc':
        cars = sorted(cars, key=lambda c: c['price'], reverse=True)

    return render(request, 'cars/car_list.html', {
        'cars': cars,
        'count': len(cars),
        'categories': sorted({c['category'] for c in CARS}),
        'selected': category,
        'sort': sort,
    })


def car_detail(request, slug):
    # نبحث عن السيارة اللي slug مالها يطابق الرابط
    car = next((c for c in CARS if c['slug'] == slug), None)
    if car is None:
        raise Http404("Car not found")
    related = [c for c in CARS if c['slug'] != slug][:3]
    return render(request, 'cars/car_detail.html', {'car': car, 'related': related})


def about(request):
    return render(request, 'cars/about.html')