
from django.shortcuts import render
from .cars_data import CARS


def home(request):
    return render(request, 'main/home.html')


def all_cars(request):
    cars = CARS.copy()

    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    year = request.GET.get('year', '')
    sort = request.GET.get('sort', '')

    if min_price:
        cars = [
            car for car in cars
            if car['price'] >= int(min_price)
        ]

    if max_price:
        cars = [
            car for car in cars
            if car['price'] <= int(max_price)
        ]

    if year:
        cars = [
            car for car in cars
            if car['year'] == int(year)
        ]

    if sort == 'low':
        cars.sort(key=lambda car: car['price'])

    elif sort == 'high':
        cars.sort(key=lambda car: car['price'], reverse=True)

    return render(request, 'main/all_cars.html', {
        'cars': cars,
        'min_price': min_price,
        'max_price': max_price,
        'selected_year': year,
        'selected_sort': sort,
    })


def about(request):
    return render(request, 'main/about.html')


def amg_gt(request):
    return render(request, 'main/cars/amg_gt.html')


def c63(request):
    return render(request, 'main/cars/c63.html')


def sl63(request):
    return render(request, 'main/cars/sl63.html')
