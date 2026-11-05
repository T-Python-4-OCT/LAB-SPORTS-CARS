from django.http import Http404
from django.shortcuts import render

CARS = [
    {
        "id": 1,
        "name": "Burgundy Luxury Sedan",
        "category": "Classic Collection",
        "description": "A refined classic sedan with timeless character.",
        "image": "main/images/masar_car_1.jpg",
        "body_style": "Classic sedan",
        "color": "Burgundy",
    },
    {
        "id": 2,
        "name": "Red Classic Pickup",
        "category": "Classic Collection",
        "description": "A vintage pickup with a bold, practical design.",
        "image": "main/images/masar_car_2.jpg",
        "body_style": "Pickup",
        "color": "Red",
    },
    {
        "id": 3,
        "name": "Golden Vintage Coupe",
        "category": "Heritage Collection",
        "description": "A golden two-door classic with elegant lines.",
        "image": "main/images/masar_car_3.jpg",
        "body_style": "Coupe",
        "color": "Gold",
    },
    {
        "id": 4,
        "name": "Rolls-Royce Classic Saloon",
        "category": "Luxury Classics",
        "description": "A distinguished classic saloon bearing the Rolls-Royce badge.",
        "image": "main/images/masar_car_4.jpg",
        "body_style": "Saloon",
        "color": "Brown",
        "manufacturer_url": "https://www.rolls-roycemotorcars.com/en_US/home.html",
    },
    {
        "id": 5,
        "name": "Black Heritage Coupe",
        "category": "Classic Collection",
        "description": "A dark classic coupe with a powerful vintage presence.",
        "image": "main/images/masar_car_5.jpg",
        "body_style": "Coupe",
        "color": "Black",
    },
    {
        "id": 6,
        "name": "Dodge Charger R/T",
        "category": "Iconic Collection",
        "description": "A blue classic coupe bearing the Charger R/T badge.",
        "image": "main/images/masar_car_6.jpg",
        "body_style": "Coupe",
        "color": "Blue",
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