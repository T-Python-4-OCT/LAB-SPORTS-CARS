from django.http import Http404
from django.shortcuts import render

from .data import CARS


def find_car(slug):
    """Return the car with the given slug, or raise Http404."""
    try:
        return next(car for car in CARS if car['slug'] == slug)
    except StopIteration:
        raise Http404('Car not found')


def home(request):
    context = {
        'featured': [car for car in CARS if car['is_featured']],
        'models': CARS,
        'total': len(CARS),
        'max_power': max(car['power'] for car in CARS),
    }
    return render(request, 'cars/home.html', context)

def car_list(request):
    category = request.GET.get('category', '')
    sort = request.GET.get('sort', '')

    cars = CARS
    if category:
        cars = [car for car in cars if car['category'] == category]

    if sort == 'price_asc':
        cars = sorted(cars, key=lambda car: car['price'])
    elif sort == 'price_desc':
        cars = sorted(cars, key=lambda car: car['price'], reverse=True)

    context = {
        'cars': cars,
        'count': len(cars),
        'categories': sorted({car['category'] for car in CARS}),
        'selected': category,
        'sort': sort,
    }
    return render(request, 'cars/car_list.html', context)


def car_detail(request, slug):
    car = find_car(slug)
    related = [other for other in CARS if other['slug'] != slug][:3]
    return render(request, 'cars/car_detail.html', {'car': car, 'related': related})


def about(request):
    return render(request, 'cars/about.html')