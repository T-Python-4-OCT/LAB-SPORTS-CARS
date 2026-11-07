from django.http import Http404
from django.shortcuts import render

CARS = [
    {"slug": "porsche-911-turbo-s", "name": "Porsche 911 Turbo S", "make": "Porsche", "english": "911 Turbo S", "year": "2025", "price": "1,295,000", "category": "Performance Coupe", "image": "https://img.autocarindia.com/Galleries/20200303050559_2020-Porsche-911-Turbo-S-si.jpg?q=90&w=1400", "short": "Iconic design, paired with exhilarating twin-turbo performance.", "engine": "3.8L Twin-Turbo", "power": "640 hp", "acceleration": "2.7 sec", "drive": "All-wheel drive", "description": "The Porsche 911 Turbo S blends everyday usability with extraordinary performance. Its unmistakable silhouette, precise handling, and twin-turbo power make every drive memorable.", "color": "Carrara White"},
    {"slug": "ferrari-f8-tributo", "name": "Ferrari F8 Tributo", "make": "Ferrari", "english": "F8 Tributo", "year": "2024", "price": "1,490,000", "category": "Mid-Engine Supercar", "image": "https://images.unsplash.com/photo-1730110206434-37f276d38675?auto=format&fit=crop&w=1200&q=85", "short": "A tribute to Ferrari's most celebrated mid-engine V8 heritage.", "engine": "3.9L Twin-Turbo V8", "power": "710 hp", "acceleration": "2.9 sec", "drive": "Rear-wheel drive", "description": "The Ferrari F8 Tributo celebrates the marque's celebrated V8 lineage with a thrilling powertrain, sculpted aerodynamic bodywork, and a driver-focused cockpit.", "color": "Rosso Corsa"},
    {"slug": "lamborghini-huracan", "name": "Lamborghini Huracán", "make": "Lamborghini", "english": "Huracán", "year": "2024", "price": "1,420,000", "category": "Supercar", "image": "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=1200&q=85", "short": "A naturally aspirated V10 with unmistakable Italian character.", "engine": "5.2L V10", "power": "631 hp", "acceleration": "2.9 sec", "drive": "All-wheel drive", "description": "The Huracán combines dramatic Italian design with the unmistakable sound and response of a naturally aspirated V10. Its focused chassis makes every road feel like an occasion.", "color": "Giallo Inti"},
]

GALLERIES = {
    "porsche-911-turbo-s": [
        "https://img.autocarindia.com/Galleries/20200303050559_2020-Porsche-911-Turbo-S-si.jpg?q=90&w=1400",
        "https://www.mclarenchicago.com/blobs/stock/57635281/images/b44dcf51-62ee-41f1-bf1e-d62714e317c2/img_7936.jpeg?height=1333&width=2000",
        "https://automanagerprodcdn.azureedge.net/wmphotos/033666/f1d13e0c4e5343c8bed70e1ed6970238/4ad37330c3_1920.jpg",
    ],
    "ferrari-f8-tributo": [
        "https://images.unsplash.com/photo-1730110206434-37f276d38675?auto=format&fit=crop&w=1400&q=90",
        "https://www.ilusso.com/imagetag/284/29/l/Used-2021-Ferrari-F8-Tributo-1636652708.jpg",
        "https://www.autocerto.com/fotos/1006/1864736/19.jpg",
    ],
    "lamborghini-huracan": [
        "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=1400&q=90",
        "https://images.unsplash.com/photo-1621285960899-ba033aeca203?auto=format&fit=crop&w=1400&q=90",
        "https://images.unsplash.com/photo-1620288989247-7bed762ccb12?auto=format&fit=crop&w=1400&q=90",
    ],
}

for car in CARS:
    car["gallery"] = GALLERIES[car["slug"]]
    car["image"] = car["gallery"][0]

def home(request):
    return render(request, "cars/home.html", {"cars": CARS})

def all_cars(request):
    return render(request, "cars/all_cars.html", {"cars": CARS})

def about(request):
    return render(request, "cars/about.html", {"cars": CARS})

def car_detail(request, slug):
    index = next((i for i, item in enumerate(CARS) if item["slug"] == slug), None)
    if index is None:
        raise Http404("Car not found")
    car = CARS[index]
    previous_car = CARS[(index - 1) % len(CARS)]
    next_car = CARS[(index + 1) % len(CARS)]
    return render(request, "cars/detail.html", {
        "car": car,
        "cars": CARS,
        "previous_car": previous_car,
        "next_car": next_car,
    })
