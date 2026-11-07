from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404, HttpResponse


CARS = [
    {
        "id": 1,
        "name": "Ferrari F8 Tributo",
        "brand": "Ferrari",
        "price": "1,490,000",
        "image": "images/ferrari.jpg",
        "gallery": [
            "images/ferrari.jpg",
            "images/ferrari_2.png",
            "images/ferrari_3.png",
            "images/ferrari_4.png",
        ],
        "engine": "3.9L V8 Twin-Turbo",
        "power": "710 hp",
        "acceleration": "2.9 s",
        "top_speed": "340 km/h",
        "headline": "The F8, Unleashed",
        "description": "A mid-rear-engined masterpiece that pushes the limits of sound, speed and handling.",
    },
    {
        "id": 2,
        "name": "Porsche 911 Turbo S",
        "brand": "Porsche",
        "price": "1,295,000",
        "image": "images/porsche.jpg",
        "gallery": [
            "images/porsche.jpg",
            "images/porsche_2.jpg",
            "images/porsche_3.jpg",
            "images/porsche_4.jpg",
        ],
        "engine": "3.8L Twin-Turbo",
        "power": "640 hp",
        "acceleration": "2.7 s",
        "top_speed": "330 km/h",
        "headline": "The Iconic 911, Elevated",
        "description": "A perfect balance of everyday usability and extraordinary performance, the 911 Turbo S delivers a driving experience like no other.",
    },
    {
        "id": 3,
        "name": "Lamborghini Huracán",
        "brand": "Lamborghini",
        "price": "1,420,000",
        "image": "images/lamborghini.jpg",
        "gallery": [
            "images/lamborghini.jpg",
            "images/lamborghini_2.jpg",
            "images/lamborghini_3.jpg",
            "images/lamborghini_4.jpg",
        ],
        "engine": "5.2L V10",
        "power": "631 hp",
        "acceleration": "2.9 s",
        "top_speed": "325 km/h",
        "headline": "Pure V10 Emotion",
        "description": "A naturally aspirated V10 and razor-sharp design make the Huracán one of the most thrilling supercars on the road.",
    },
]

PRICE_RANGES = {
    "low": {"label": "Under 1,300,000", "min": 0, "max": 1300000},
    "mid": {"label": "1,300,000 - 1,450,000", "min": 1300000, "max": 1450000},
    "high": {"label": "Above 1,450,000", "min": 1450000, "max": None},
}


def home_view(request: HttpRequest):
    return render(request, 'main/home.html', {"cars": CARS})



def cars_view(request: HttpRequest):
    selected_brand = request.GET.get("brand", "")
    selected_price = request.GET.get("price", "")

    cars = CARS

    if selected_brand:
        cars = [c for c in cars if c["brand"] == selected_brand]

    if selected_price in PRICE_RANGES:
        r = PRICE_RANGES[selected_price]
        cars = [
            c for c in cars
            if int(c["price"].replace(",", "")) >= r["min"]
            and (r["max"] is None or int(c["price"].replace(",", "")) < r["max"])
        ]

    context = {
        "cars": cars,
        "brands": sorted({c["brand"] for c in CARS}),
        "price_ranges": [{"key": k, "label": v["label"]} for k, v in PRICE_RANGES.items()],
        "selected_brand": selected_brand,
        "selected_price": selected_price,
    }
    return render(request, 'main/cars.html', context)



def car_detail_view(request: HttpRequest, car_id):
    car = next((c for c in CARS if c["id"] == car_id), None)
    if car is None:
        raise Http404("Car not found")
    return render(request, 'main/car_detail.html', {"car": car})


def mode_view(request: HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")

    return response


def about_view(request: HttpRequest):
    return render(request, 'main/about.html')