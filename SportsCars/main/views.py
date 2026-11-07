
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

CARS = [
    {"slug": "porsche-911-carrera-rs", "name": "Porsche 911 Carrera RS 2.7", "year": "1973",
     "price": "2,450,000", "engine": "2.7L Flat-Six", "power": "210 hp",
     "accel": "5.8 s", "top_speed": "245 km/h",
      },

    {"slug": "ferrari-250-gto", "name": "Ferrari 250 GTO", "year": "1962",
     "price": "150,000,000", "engine": "3.0L V12", "power": "300 hp",
     "accel": "6.1 s", "top_speed": "280 km/h",
     },

    {"slug": "jaguar-e-type", "name": "Jaguar E-Type", "year": "1961",
     "price": "520,000", "engine": "3.8L Inline-6", "power": "265 hp",
     "accel": "7.0 s", "top_speed": "240 km/h",
     },

    {"slug": "lamborghini-miura", "name": "Lamborghini Miura P400 S", "year": "1969",
     "price": "9,400,000", "engine": "3.9L V12", "power": "370 hp",
     "accel": "6.7 s", "top_speed": "280 km/h",
     },

    {"slug": "mercedes-300-sl", "name": "Mercedes-Benz 300 SL Gullwing", "year": "1954",
     "price": "4,500,000", "engine": "3.0L Inline-6", "power": "215 hp",
     "accel": "8.8 s", "top_speed": "260 km/h",
     },
     
    {"slug": "ford-mustang-fastback", "name": "Ford Mustang Fastback GT", "year": "1968",
               "price": "650,000", "engine": "4.9L V8", "power": "335 hp",
               "accel": "6.5 s", "top_speed": "210 km/h",
     },

      


]

for c in CARS:
    c["image"] = f"images/cars/{c['slug']}.jpg"
    c["gallery"] = [c["image"]] + [
        f"images/cars/{c['slug']}/{i}.jpg" for i in range(2, 5)
    ]
DEFAULT_FEATURES = [
    {"icon": "airline_seat_recline_extra", "title": "Classic Interior", "text": "Authentic cabin with period-correct materials."},
    {"icon": "tire_repair", "title": "Iconic Design", "text": "Timeless lines that defined an era."},
    {"icon": "history", "title": "Verified History", "text": "Full documentation and inspection report."},
]

for c in CARS:
    c.setdefault("features", DEFAULT_FEATURES)



def home(request: HttpRequest):
    return render(request, "main/home.html", {"featured": CARS[:3]})


def all_cars(request: HttpRequest):
    selected_model = request.GET.get("model", "")
    selected_sort = request.GET.get("sort", "")

    cars = CARS

    if selected_model:
        cars = [c for c in cars if c["slug"] == selected_model]

    if selected_sort in ("price_asc", "price_desc"):
        cars = sorted(
            cars,
            key=lambda c: int(c["price"].replace(",", "")),
            reverse=(selected_sort == "price_desc"),
        )

    return render(request, "main/all_cars.html", {
        "cars": cars,
        "models": CARS,
        "selected_model": selected_model,
        "selected_sort": selected_sort,
    })



def car_detail(request: HttpRequest, slug):
    car = next((c for c in CARS if c["slug"] == slug), None)
    if car is None:
        raise Http404("Car not found")
    return render(request, "main/car_detail.html", {"car": car})


def about(request: HttpRequest):
    return render(request, "main/about.html")


def mode_view(request: HttpRequest, mode):
    next_url = request.GET.get("next", "/")

    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = "/"

    response = redirect(next_url)

    if mode in ("light", "dark"):
        response.set_cookie("mode", mode, max_age=60 * 60 * 24 * 365)

    return response
