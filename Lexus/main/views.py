from django.shortcuts import redirect, render


def car(key, name, year, price, specs=None, description=""):
    data = {
        "slug": "lexus-" + name.lower().replace(" ", "-"),
        "name": f"Lexus {name}",
        "year": year,
        "price": price,
        "image": f"images/{key}_card.jpg",
        "has_detail": bool(specs),
    }
    if specs:
        engine, power, acceleration, top_speed = specs
        data.update(
            engine=engine,
            power=power,
            acceleration=acceleration,
            top_speed=top_speed,
            description=description,
            gallery=[f"images/{key}_{part}.jpg" for part in ("card", "detail", "feature", "gallery1")],
        )
    return data


CARS = [
    car(
        "es", "ES 300h", 2025, "SAR 198,720", ("2.5L I4 Hybrid", 214, "8.9 s", 180),
        "An elegant executive sedan that blends Lexus comfort, advanced hybrid efficiency, and a quiet premium cabin.",
    ),
    car(
        "is", "IS 350", 2026, "SAR 216,947.50", ("3.5L V6", 311, "Approx. 6.0 s", 230),
        "A sharp and athletic sedan with strong V6 performance, bold Lexus styling, and a driver-focused character.",
    ),
    car(
        "nx", "NX 350h", 2026, "SAR 234,255", ("2.5L I4 Hybrid", 240, "7.7 s", 200),
        "A modern compact SUV with expressive design, efficient hybrid performance, and the latest Lexus technology.",
    ),
    car("rx", "RX 350h", 2026, "SAR 322,230"),
    car("lx", "LX 600", 2026, "SAR 595,412.50"),
    car("lc", "LC 500", 2026, "SAR 488,807.50"),
]


def home(request):
    return render(request, "home.html", {"featured": CARS[:3]})


def cars(request):
    return render(request, "cars.html", {"cars": CARS})


def car_detail(request, slug):
    car = next((c for c in CARS if c["slug"] == slug and c["has_detail"]), None)
    if car is None:
        return redirect("cars")

    count = len(car["gallery"])
    gallery = [
        {"n": n, "photo": photo, "prev": (n - 2) % count + 1, "next": n % count + 1}
        for n, photo in enumerate(car["gallery"], 1)
    ]
    specs = [
        ("settings", "Engine", car["engine"], "Engine"),
        ("bolt", "Power", f"{car['power']} hp", "Max Power"),
        ("timer", "0–100 km/h", car["acceleration"], "0–100 km/h"),
        ("speed", "Top Speed", f"{car['top_speed']} km/h", "Top Speed"),
    ]
    return render(request, "car_detail.html", {"car": car, "gallery": gallery, "specs": specs})


def about(request):
    return render(request, "about.html")


def toggle_theme(request):
    theme = "light" if request.COOKIES.get("theme") == "dark" else "dark"
    next_url = request.GET.get("next", "/")
    if not next_url.startswith("/") or next_url.startswith("//"):
        next_url = "/"

    response = redirect(next_url)
    response.set_cookie("theme", theme, max_age=60 * 60 * 24 * 365, samesite="Lax")
    return response