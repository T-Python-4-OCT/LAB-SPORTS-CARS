# بيانات السيارات الرياضية من فورد.
# "slug" يظهر في الرابط، فلازم يكون فريد وبدون مسافات.
# الأسعار المعلّمة (تقديري) راجعها من موقع وكيل فورد قبل التسليم.
CARS = [
    # ===== أول 3 سيارات = المميزة في الصفحة الرئيسية (rank 1-3) =====
    {"slug": "ford-mustang-gt", "name": "Ford Mustang GT", "category": "Coupe", "rank": 1,
     "price": 224003, "year": 2026, "engine": "5.0L V8", "power": 480, "seats": 4,
     "drive": "RWD", "image": "images/mustang-gt.jpg",
     "tagline": "The American Icon",
     "description": "The legendary V8 coupe: naturally aspirated power, a thunderous exhaust and pure driving feel."},

    {"slug": "ford-mustang-dark-horse", "name": "Ford Mustang Dark Horse", "category": "Coupe", "rank": 2,
     "price": 345000, "year": 2026, "engine": "5.0L V8", "power": 500, "seats": 4,        # سعر تقديري
     "drive": "RWD", "image": "images/dark-horse.jpg",
     "tagline": "Track-Ready Performance",
     "description": "The most extreme Mustang: sharper handling, upgraded brakes and a 500 hp V8 built for the circuit."},

    {"slug": "ford-explorer-st", "name": "Ford Explorer ST", "category": "SUV", "rank": 3,
     "price": 236900, "year": 2026, "engine": "3.0L Twin-Turbo V6", "power": 400, "seats": 7,
     "drive": "AWD", "image": "images/explorer-st.jpg",
     "tagline": "Sport Meets Family",
     "description": "A seven-seat performance SUV with a twin-turbo V6, sport-tuned suspension and all-wheel drive."},

    # ===== باقي السيارات (لصفحة All Cars) =====
    {"slug": "ford-edge-st", "name": "Ford Edge ST", "category": "SUV", "rank": 4,
     "price": 167895, "year": 2026, "engine": "2.7L EcoBoost V6", "power": 335, "seats": 5,
     "drive": "AWD", "image": "images/edge-st.jpg",
     "tagline": "Everyday Sport",
     "description": "A sporty five-seat SUV with strong V6 power and sharp, confident handling."},

    {"slug": "ford-ranger-raptor", "name": "Ford Ranger Raptor", "category": "Pickup", "rank": 5,
     "price": 276000, "year": 2026, "engine": "3.0L Twin-Turbo V6", "power": 392, "seats": 5,
     "drive": "4WD", "image": "images/ranger-raptor.jpg",
     "tagline": "Built to Fly Over Dunes",
     "description": "A high-performance pickup with race-tuned suspension, made for fast desert driving."},

    {"slug": "ford-f150-raptor", "name": "Ford F-150 Raptor", "category": "Pickup", "rank": 6,
     "price": 412855, "year": 2026, "engine": "3.5L EcoBoost V6", "power": 450, "seats": 5,   # راجع السعر
     "drive": "4WD", "image": "images/f150-raptor.jpg",
     "tagline": "Desert Dominator",
     "description": "The ultimate full-size performance truck, with long-travel suspension and 450 hp."},

    {"slug": "ford-bronco-raptor", "name": "Ford Bronco Raptor", "category": "Off-Road", "rank": 7,
     "price": 428696, "year": 2026, "engine": "3.0L Twin-Turbo V6", "power": 418, "seats": 4,  # سعر تقديري
     "drive": "4WD", "image": "images/bronco-raptor.jpg",
     "tagline": "Born Wild, Built Fast",
     "description": "The most capable Bronco ever: wide stance, race-grade shocks and serious off-road speed."},
]