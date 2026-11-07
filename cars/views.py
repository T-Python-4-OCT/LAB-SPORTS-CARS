
import json
from pathlib import Path

from django.http import Http404
from django.shortcuts import render


DATA_FILE = Path(__file__).resolve().parent / "data" / "cars.json"

with DATA_FILE.open(encoding="utf-8") as file:
    cars = json.load(file)


def all_cars(request):
    return render(request, "cars/all_cars.html", {"cars": cars})


def car_detail(request, car_id):
    car = next((item for item in cars if item["id"] == car_id), None)

    if car is None:
        raise Http404("Car not found")

    return render(request, "cars/car_detail.html", {"car": car})
