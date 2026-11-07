"""
Car data used by the templates (no database needed for this lab).
`image` paths are relative to the static folder.
"""

CARS = [
    {
        "slug": "porsche-911-turbo-s",
        "price_value": 1295000,
        "transmission": "8-speed PDK",
        "drivetrain": "All-Wheel Drive",
        "weight": "1,640 kg",
        "name": "Porsche 911 Turbo S",
        "brand": "Porsche",
        "year": 2025,
        "price": "SAR 1,295,000",
        "image": "main/images/porsche-911-turbo-s.jpg",
        "gallery": ["main/images/porsche-911-turbo-s.jpg", "main/images/hero.jpg", "main/images/interior.jpg"],
        "engine": "3.8 L Twin-Turbo",
        "power": "640 hp",
        "acceleration": "2.7 s",
        "top_speed": "330 km/h",
        "tagline": "The Iconic 911, Elevated",
        "description": "A perfect balance of everyday usability and extraordinary performance, the 911 Turbo S delivers a driving experience like no other.",
        "has_detail": True,
    },
    {
        "slug": "porsche-911-gt3",
        "price_value": 1050000,
        "transmission": "7-speed PDK",
        "drivetrain": "Rear-Wheel Drive",
        "weight": "1,435 kg",
        "name": "Porsche 911 GT3",
        "brand": "Porsche",
        "year": 2025,
        "price": "SAR 1,050,000",
        "image": "main/images/porsche-911-gt3.jpg",
        "gallery": ["main/images/porsche-911-gt3.jpg", "main/images/porsche-911-gt3-rain.jpg", "main/images/interior-dark.jpg"],
        "engine": "4.0 L Flat-Six",
        "power": "510 hp",
        "acceleration": "3.4 s",
        "top_speed": "318 km/h",
        "tagline": "Born on the Track",
        "description": "A naturally aspirated flat-six that revs to 9,000 rpm, motorsport-bred aerodynamics and razor-sharp handling make the GT3 a true driver's car.",
        "has_detail": True,
    },
    {
        "slug": "porsche-taycan-turbo-s",
        "price_value": 980000,
        "transmission": "2-speed Automatic",
        "drivetrain": "All-Wheel Drive",
        "weight": "2,295 kg",
        "name": "Porsche Taycan Turbo S",
        "brand": "Porsche",
        "year": 2025,
        "price": "SAR 980,000",
        "image": "main/images/porsche-taycan.jpg",
        "gallery": ["main/images/porsche-taycan.jpg", "main/images/road-night.jpg", "main/images/interior-red.jpg"],
        "engine": "Dual Electric Motors",
        "power": "952 hp",
        "acceleration": "2.4 s",
        "top_speed": "260 km/h",
        "tagline": "Electric, Unmistakably Porsche",
        "description": "Instant torque, a sculpted silhouette and Porsche DNA in every detail: the Taycan Turbo S proves electric can be thrilling.",
        "has_detail": True,
    },
    {
        "slug": "porsche-911-gt3-rs",
        "price_value": 1420000,
        "name": "Porsche 911 GT3 RS",
        "brand": "Porsche",
        "year": 2024,
        "price": "SAR 1,420,000",
        "image": "main/images/porsche-gt3-rs.jpg",
        "has_detail": False,
    },
    {
        "slug": "porsche-911-carrera",
        "price_value": 690000,
        "name": "Porsche 911 Carrera",
        "brand": "Porsche",
        "year": 2024,
        "price": "SAR 690,000",
        "image": "main/images/white-sports-car.jpg",
        "has_detail": False,
    },
    {
        "slug": "porsche-911-gt3-cup",
        "price_value": 1150000,
        "name": "Porsche 911 GT3 Cup",
        "brand": "Porsche",
        "year": 2023,
        "price": "SAR 1,150,000",
        "image": "main/images/porsche-race.jpg",
        "has_detail": False,
    },
]


KEY_FEATURES = [
    {"title": "Premium Interior", "text": "A driver-focused cabin with refined materials.", "image": "main/images/interior.jpg"},
    {"title": "Sport Cockpit", "text": "Every control placed for precision and control.", "image": "main/images/interior-dark.jpg"},
    {"title": "Aerodynamic Design", "text": "Engineered for maximum stability and performance.", "image": "main/images/porsche-911-gt3-rain.jpg"},
]


def get_car(slug):
    for car in CARS:
        if car["slug"] == slug and car.get("has_detail"):
            return car
    return None


def featured_cars():
    return [c for c in CARS if c.get("has_detail")]
