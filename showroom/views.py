from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_GET
from .data import VEHICLES, VEHICLES_BY_SLUG


@require_GET
def home(request):
    return render(request, "showroom/home.html", {"vehicles": VEHICLES, "active": "home"})


@require_GET
def cars(request):
    return render(request, "showroom/cars.html", {"vehicles": VEHICLES, "active": "cars"})


@require_GET
def detail(request, slug):
    vehicle = VEHICLES_BY_SLUG.get(slug)
    if not vehicle:
        raise Http404("This model is not available in the demo showroom.")
    return render(request, "showroom/detail.html", {
        "vehicle": vehicle, "active": "cars",
    })


@require_GET
def about(request):
    return render(request, "showroom/about.html", {"active": "about"})
