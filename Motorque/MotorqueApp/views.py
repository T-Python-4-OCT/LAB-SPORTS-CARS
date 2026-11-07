
from django.shortcuts import render
from django.http import HttpRequest


CARS = [
    {
        'name': 'Porsche 911 Carrera',
        'brand': 'Porsche',
        'model': '911 Carrera',
        'category': 'Sports Car',
        'price': 650000,
        'image': 'MotorqueApp/images/Porsche911/Contrast/Black/911-ContrastBlack1.jpeg',
    },
    {
        'name': 'Genesis G80',
        'brand': 'Genesis',
        'model': 'G80',
        'category': 'Luxury Sedan',
        'price': 230000,
        'image': 'MotorqueApp/images/G80/G80-HeaderBlack.png',
    },
    {
        'name': 'Cadillac Escalade',
        'brand': 'Cadillac',
        'model': 'Escalade',
        'category': 'Luxury SUV',
        'price': 550000,
        'image': 'MotorqueApp/images/Escalade/Escalade 2.jpg',
    },
]


def home(request: HttpRequest):
    return render(request, 'MotorqueApp/home.html', {
        'cars': CARS
    })


def all_cars(request: HttpRequest):
    return render(request, 'MotorqueApp/all_cars.html', {
        'cars': CARS
    })


def genesis_g80(request: HttpRequest):
    return render(request, 'MotorqueApp/car_detail.html')


def porsche_911(request: HttpRequest):
    return render(request, 'MotorqueApp/porsche_detail.html')


def cadillac_escalade(request: HttpRequest):
    return render(request, 'MotorqueApp/escalade_detail.html')

def about_us(request: HttpRequest):
    return render(request, 'MotorqueApp/about_us.html')