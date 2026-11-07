from django.http import Http404
from django.shortcuts import render

CARS = [
    {
        "id": 1,
        "name": "Cadillac Fleetwood Brougham",
        "brand": "Cadillac",
        "price": 35000,
        "category": "Luxury Classics",
        "description": "A 1984 luxury sedan with a 4.1L V8 engine producing about 135 HP.",
        "image": "main/images/masar_car_1.jpg",
        "body_style": "Luxury full-size sedan",
        "color": "Burgundy",
        "year": 1984,
        "model": "Fleetwood Brougham",
        "engine": "4.1L V8",
        "horsepower": "135 HP",
        "top_speed": "Approximately 180 km/h",
        "manufacturer_url": "https://www.cadillac.com/",
    },
    {
        "id": 2,
        "name": "Chevrolet C20",
        "brand": "Chevrolet",
        "price": 65000,
        "category": "Classic Collection",
        "description": "A 1976 classic pickup powered by a 5.7L V8 engine.",
        "image": "main/images/masar_car_2.jpg",
        "body_style": "Classic pickup truck",
        "color": "Red",
        "year": 1976,
        "model": "C20",
        "engine": "5.7L V8 (350)",
        "horsepower": "Approximately 175 HP",
        "top_speed": "Approximately 160 km/h",
        "manufacturer_url": "https://www.chevrolet.com/",
    },
    {
        "id": 3,
        "name": "Nissan Skyline 2000GT-X",
        "brand": "Nissan",
        "price": 180000,
        "category": "Heritage Collection",
        "description": "A 1973 classic sports coupe with a 2.0L inline-six engine.",
        "image": "main/images/masar_car_3.jpg",
        "body_style": "Classic sports coupe",
        "color": "Gold",
        "year": 1973,
        "model": "Skyline 2000GT-X",
        "engine": "2.0L Inline-6",
        "horsepower": "Approximately 130 HP",
        "top_speed": "Approximately 180 km/h",
        "manufacturer_url": "https://www.nissan-global.com/EN/",
    },
    {
        "id": 4,
        "name": "Rolls-Royce 20/25 HP",
        "brand": "Rolls-Royce",
        "price": 280000,
        "category": "Luxury Classics",
        "description": "A 1932 luxury vintage saloon with a 3.7L inline-six engine.",
        "image": "main/images/masar_car_4.jpg",
        "body_style": "Luxury vintage sedan",
        "color": "Brown",
        "year": 1932,
        "model": "20/25 HP",
        "engine": "3.7L Inline-6",
        "horsepower": "Approximately 65 HP (estimated)",
        "top_speed": "Approximately 120 km/h",
        "manufacturer_url": "https://www.rolls-roycemotorcars.com/en_US/home.html",
    },
    {
        "id": 5,
        "name": "Dodge Coronet R/T",
        "brand": "Dodge",
        "price": 210000,
        "category": "Classic Collection",
        "description": "A 1968 muscle-car coupe powered by the 440 Magnum V8.",
        "image": "main/images/masar_car_5.jpg",
        "body_style": "Muscle car coupe",
        "color": "Black",
        "year": 1968,
        "model": "Coronet R/T",
        "engine": "7.2L V8 (440 Magnum)",
        "horsepower": "375 HP",
        "top_speed": "Approximately 200 km/h",
        "manufacturer_url": "https://www.dodge.com/",
    },
    {
        "id": 6,
        "name": "Dodge Charger R/T",
        "brand": "Dodge",
        "price": 240000,
        "category": "Iconic Collection",
        "description": "A 1968 classic muscle coupe powered by the 440 Magnum V8.",
        "image": "main/images/masar_car_6.jpg",
        "body_style": "Muscle car coupe",
        "color": "Blue",
        "year": 1968,
        "model": "Charger R/T",
        "engine": "7.2L V8 (440 Magnum)",
        "horsepower": "375 HP",
        "top_speed": "Approximately 210 km/h",
        "manufacturer_url": "https://www.dodge.com/",
    },
]


def home(request):
    return render(request, "main/home.html")


def all_cars(request):
    return render(request, "main/all_cars.html", {"cars": CARS})


def car_detail(request, car_id):
    car = next((item for item in CARS if item["id"] == car_id), None)

    if car is None:
        raise Http404("Car not found")

    return render(request, "main/car_detail.html", {"car": car})


def about(request):
    return render(request, "main/about.html")