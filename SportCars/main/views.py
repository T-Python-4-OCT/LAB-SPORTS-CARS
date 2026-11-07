from urllib.parse import quote, unquote

from django.core.paginator import Paginator
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

# Create your views here.


# ============================================================ cars data
# (no database in this lab, so the cars live in a simple list)

def make_car(slug, brand, name, year, price, engine, power, acceleration, top_speed, headline, overview, images):
    return {
        "slug": slug, "brand": brand, "name": name, "year": year, "price": price,
        "engine": engine, "power": power, "acceleration": acceleration, "top_speed": top_speed,
        "headline": headline, "overview": overview,
        "image": f"images/cars/{images[0]}.jpg",
        "gallery": [f"images/cars/{image}.jpg" for image in images],
    }


CARS = [
    make_car("porsche-911-carrera-s", "Porsche", "911 Carrera S", 2019, 620000,
             "3.0 L Twin-Turbo Flat-6", 450, 3.5, 308,
             "The Everyday Icon",
             "The 992-generation 911 balances daily comfort with razor-sharp handling. "
             "A twin-turbo flat-six, rear-engine balance and timeless design.",
             ["porsche-911-front", "porsche-911-rear"]),
    make_car("ferrari-f8-tributo", "Ferrari", "F8 Tributo", 2020, 1490000,
             "3.9 L Twin-Turbo V8", 720, 2.9, 340,
             "A Tribute to the V8",
             "The F8 Tributo celebrates Ferrari's most awarded V8 engine. Sharp aerodynamics, "
             "instant throttle response and a chassis tuned for pure driving pleasure.",
             ["ferrari-f8-front", "ferrari-f8-rear"]),
    make_car("lamborghini-huracan-evo", "Lamborghini", "Huracán EVO", 2019, 1420000,
             "5.2 L V10", 640, 2.9, 325,
             "Naturally Aspirated Drama",
             "A screaming V10, bold Italian design and razor-sharp handling. The Huracán EVO turns "
             "every drive into an event, on the road or on the track.",
             ["huracan-front", "huracan-rear"]),
    make_car("lamborghini-aventador-s", "Lamborghini", "Aventador S", 2018, 1950000,
             "6.5 L V12", 740, 2.9, 350,
             "The V12 Flagship",
             "Scissor doors, a naturally aspirated V12 and four-wheel steering. "
             "The Aventador S is pure theatre on wheels.",
             ["aventador-front", "aventador-rear"]),
    make_car("mclaren-720s", "McLaren", "720S", 2018, 1390000,
             "4.0 L Twin-Turbo V8", 720, 2.9, 341,
             "Engineered Without Compromise",
             "A carbon-fibre monocage, active aerodynamics and a twin-turbo V8. The 720S is "
             "McLaren's answer to the question: how fast can a road car really be?",
             ["mclaren-720s"]),
    make_car("aston-martin-vantage", "Aston Martin", "Vantage", 2019, 690000,
             "4.0 L Twin-Turbo V8", 510, 3.6, 314,
             "British Grand Touring",
             "Hand-built elegance meets a muscular V8. The Vantage pairs timeless British style "
             "with a playful, rear-driven character.",
             ["vantage-front", "vantage-rear"]),
    make_car("audi-r8-v10-plus", "Audi", "R8 V10 plus", 2018, 780000,
             "5.2 L V10", 610, 3.2, 330,
             "The Everyday Supercar",
             "A mid-mounted V10 shared with Lamborghini, quattro all-wheel drive and a cabin "
             "you can live with every day.",
             ["r8-front", "r8-rear"]),
    make_car("bmw-m8-competition", "BMW", "M8 Competition", 2019, 720000,
             "4.4 L Twin-Turbo V8", 625, 3.2, 305,
             "Luxury at Full Throttle",
             "Grand-tourer comfort with M Division muscle. The M8 Competition covers continents "
             "in luxury and still devours a racetrack.",
             ["m8-front", "m8-rear"]),
    make_car("chevrolet-corvette-stingray", "Chevrolet", "Corvette Stingray", 2023, 420000,
             "6.2 L V8", 495, 2.9, 312,
             "America Goes Mid-Engine",
             "The C8 Corvette moved its V8 behind the driver for the first time, delivering "
             "supercar performance at a fraction of the price.",
             ["corvette-front", "corvette-rear"]),
    make_car("mercedes-amg-gt-r", "Mercedes-AMG", "GT R", 2019, 750000,
             "4.0 L Twin-Turbo V8", 585, 3.6, 318,
             "The Beast of the Green Hell",
             "Developed on the Nürburgring, the AMG GT R combines rear-wheel steering, "
             "adjustable suspension and a hand-crafted V8 for serious track pace.",
             ["amg-gtr"]),
]

KEY_FEATURES = [
    {"icon": "airline_seat_recline_extra", "title": "Premium Interior", "text": "A driver-focused cabin with refined materials."},
    {"icon": "tire_repair", "title": "Performance Brakes", "text": "Exceptional stopping power and control."},
    {"icon": "air", "title": "Aerodynamic Design", "text": "Engineered for maximum stability and performance."},
]

# value -> (label, min, max)
PRICE_RANGES = {
    "under-700k": ("Under SAR 700K", 0, 700000),
    "700k-1.4m": ("SAR 700K – 1.4M", 700000, 1400000),
    "over-1.4m": ("Over SAR 1.4M", 1400000, None),
}

FEATURED_BRANDS = ["Porsche", "Ferrari", "Lamborghini", "McLaren"]

ONE_YEAR = 60 * 60 * 24 * 365


# ============================================================ helpers

def get_car(slug):
    """Return the car with this slug, or None."""
    for car in CARS:
        if car["slug"] == slug:
            return car
    return None


def get_car_or_404(slug):
    car = get_car(slug)
    if car is None:
        raise Http404("Car not found")
    return car


def get_next_url(request: HttpRequest):
    """Read the ?next= query parameter, and only allow links to our own site."""
    next_url = request.GET.get("next", "/")
    if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        return next_url
    return "/"


def get_ratings(request: HttpRequest):
    """Cookie "ratings" looks like "porsche-911-carrera-s:4|ferrari-f8-tributo:5"."""
    ratings = {}
    for item in request.COOKIES.get("ratings", "").split("|"):
        slug, _, stars = item.partition(":")
        if stars.isdigit() and 1 <= int(stars) <= 5:
            ratings[slug] = int(stars)
    return ratings


def with_cookie_info(request: HttpRequest, cars):
    """Copy each car and add "saved" (wishlist cookie) and "rating" (ratings cookie)."""
    wishlist = request.COOKIES.get("wishlist", "").split("|")
    ratings = get_ratings(request)
    return [{**car, "saved": car["slug"] in wishlist, "rating": ratings.get(car["slug"])} for car in cars]


def get_recently_viewed(request: HttpRequest):
    """Signed cookie: if someone edits it by hand, Django ignores it and we get the default."""
    value = request.get_signed_cookie("recently_viewed", default="", salt="recently-viewed")
    return [slug for slug in value.split("|") if get_car(slug)]


def compare_cars(car, other):
    """Rows for the comparison table. winner = "first", "second" or "" for a tie."""
    rows = [
        ("Year", car["year"], other["year"], "max"),
        ("Price", car["price"], other["price"], "min"),
        ("Power (hp)", car["power"], other["power"], "max"),
        ("0 – 100 km/h (s)", car["acceleration"], other["acceleration"], "min"),
        ("Top Speed (km/h)", car["top_speed"], other["top_speed"], "max"),
    ]
    comparison = []
    for label, a, b, better in rows:
        if a == b:
            winner = ""
        elif (a > b) == (better == "max"):
            winner = "first"
        else:
            winner = "second"
        if label == "Price":
            a, b = f"SAR {a:,}", f"SAR {b:,}"
        comparison.append({"label": label, "first": a, "second": b, "winner": winner})
    return comparison


# ============================================================ pages

def home_view(request: HttpRequest):

    # Query parameter: /?featured=Ferrari  -> the brand tabs above "Featured Cars"
    featured_brand = request.GET.get("featured", "")
    if featured_brand in FEATURED_BRANDS:
        featured_cars = [car for car in CARS if car["brand"] == featured_brand][:3]
    else:
        featured_brand = ""
        featured_cars = CARS[:3]

    recent_cars = [get_car(slug) for slug in get_recently_viewed(request)]

    return render(request, "main/index.html", {
        "featured_cars": with_cookie_info(request, featured_cars),
        "featured_brand": featured_brand,
        "featured_brands": FEATURED_BRANDS,
        "brands": sorted({car["brand"] for car in CARS}),
        "recent_cars": recent_cars,
    })


def cars_view(request: HttpRequest):

    # Query parameters: /cars/?brand=Porsche&price=under-700k&sort=price-asc&page=2
    brand = request.GET.get("brand", "")
    year = request.GET.get("year", "")
    price = request.GET.get("price", "")
    sort = request.GET.get("sort", "")
    search = request.GET.get("q", "").strip()
    saved_only = request.GET.get("saved") == "1"

    cars = with_cookie_info(request, CARS)

    if brand:
        cars = [car for car in cars if car["brand"] == brand]

    if year.isdigit():
        cars = [car for car in cars if car["year"] == int(year)]

    if price in PRICE_RANGES:
        _, low, high = PRICE_RANGES[price]
        cars = [car for car in cars if car["price"] >= low and (high is None or car["price"] < high)]

    if search:
        cars = [car for car in cars if search.lower() in f"{car['brand']} {car['name']}".lower()]

    if saved_only:
        cars = [car for car in cars if car["saved"]]

    if sort == "price-asc":
        cars = sorted(cars, key=lambda car: car["price"])
    elif sort == "price-desc":
        cars = sorted(cars, key=lambda car: car["price"], reverse=True)
    elif sort == "newest":
        cars = sorted(cars, key=lambda car: car["year"], reverse=True)

    page_obj = Paginator(cars, 6).get_page(request.GET.get("page"))

    return render(request, "main/cars.html", {
        "page_obj": page_obj,
        "total": len(cars),
        "brands": sorted({car["brand"] for car in CARS}),
        "years": sorted({car["year"] for car in CARS}, reverse=True),
        "price_ranges": {key: value[0] for key, value in PRICE_RANGES.items()},
        "selected": {"brand": brand, "year": year, "price": price, "sort": sort, "q": search, "saved": saved_only},
    })


def car_detail_view(request: HttpRequest, car_slug):

    # Path parameter (slug): /cars/porsche-911-carrera-s/
    car = with_cookie_info(request, [get_car_or_404(car_slug)])[0]
    other_cars = with_cookie_info(request, [other for other in CARS if other["slug"] != car_slug][:3])

    # Query parameter: ?compare=ferrari-f8-tributo  -> show a comparison table on this page
    compare_car = get_car(request.GET.get("compare", ""))
    if compare_car and compare_car["slug"] == car_slug:
        compare_car = None

    # Query parameters from the inquiry form: ?name=...&phone=...&message=...
    inquiry = {
        "name": request.GET.get("name", "").strip(),
        "phone": request.GET.get("phone", "").strip(),
        "message": request.GET.get("message", "").strip(),
    }
    inquiry_sent = False
    inquiry_errors = []
    if "name" in request.GET:
        if not inquiry["name"]:
            inquiry_errors.append("Please enter your name.")
        if not inquiry["phone"].replace("+", "").replace(" ", "").isdigit() or len(inquiry["phone"]) < 9:
            inquiry_errors.append("Please enter a valid phone number.")
        inquiry_sent = not inquiry_errors

    response = render(request, "main/car_detail.html", {
        "car": car,
        "key_features": KEY_FEATURES,
        "other_cars": other_cars,
        "compare_car": compare_car,
        "comparison": compare_cars(car, compare_car) if compare_car else None,
        "inquiry": inquiry,
        "inquiry_sent": inquiry_sent,
        "inquiry_errors": inquiry_errors,
        "customer_name": unquote(request.COOKIES.get("customer_name", "")),
        "stars": range(1, 6),
    })

    # Cookie: remember the visitor's name to greet them next time (URL-encoded so Arabic names work)
    if inquiry_sent:
        response.set_cookie("customer_name", quote(inquiry["name"]), max_age=ONE_YEAR)

    # Signed cookie: remember the last 3 cars this visitor opened (newest first)
    recent = [slug for slug in get_recently_viewed(request) if slug != car_slug]
    recent.insert(0, car_slug)
    response.set_signed_cookie("recently_viewed", "|".join(recent[:3]), salt="recently-viewed", max_age=ONE_YEAR)

    return response


def about_view(request: HttpRequest):

    return render(request, "main/about.html")


# ============================================================ cookies

def mode_view(request: HttpRequest, mode):

    # Path parameter (str): /mode/dark/?next=/cars/
    response = redirect(get_next_url(request))

    if mode == "light":
        response.set_cookie("mode", "light", max_age=ONE_YEAR)
    elif mode == "dark":
        response.set_cookie("mode", "dark", max_age=ONE_YEAR)

    return response


def wishlist_view(request: HttpRequest, car_slug):
    """Add the car to the wishlist cookie, or remove it if it's already there."""
    get_car_or_404(car_slug)

    wishlist = [slug for slug in request.COOKIES.get("wishlist", "").split("|") if get_car(slug)]

    if car_slug in wishlist:
        wishlist.remove(car_slug)
    else:
        wishlist.append(car_slug)

    response = redirect(get_next_url(request))

    if wishlist:
        response.set_cookie("wishlist", "|".join(wishlist), max_age=ONE_YEAR)
    else:
        response.delete_cookie("wishlist")

    return response


def rate_view(request: HttpRequest, car_slug, stars):

    # Path parameters (slug + int): /rate/porsche-911-carrera-s/4/  -> stars arrives as an int
    get_car_or_404(car_slug)
    if not 1 <= stars <= 5:
        raise Http404("Rating must be between 1 and 5")

    ratings = get_ratings(request)
    ratings[car_slug] = stars

    response = redirect(get_next_url(request))
    response.set_cookie("ratings", "|".join(f"{slug}:{value}" for slug, value in ratings.items()), max_age=ONE_YEAR)

    return response


def forget_me_view(request: HttpRequest):
    """Delete every cookie this site saved."""
    response: HttpResponse = redirect(get_next_url(request))

    for key in ("mode", "wishlist", "recently_viewed", "customer_name", "ratings"):
        response.delete_cookie(key)

    return response
