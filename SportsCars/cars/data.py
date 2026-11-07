def _car(slug, name, price, year, category, engine, power, accel, top, drive, desc, features):
    return {
        "slug": slug, "name": name, "price": price, "year": year,
        "category": category, "engine": engine, "power": power,
        "accel": accel, "top_speed": top, "drivetrain": drive,
        "desc": desc, "features": features,
        "img": f"images/cars/{slug}.jpg",
        "gallery": [f"images/cars/{slug}.jpg",
                    f"images/cars/{slug}-2.jpg",
                    f"images/cars/{slug}-3.jpg"],
    }


CATEGORIES = ["Coupe", "Sedan", "SUV", "Electric"]

CARS = [
    _car("m4-competition", "BMW M4 Competition", 489000, 2025, "Coupe",
         "3.0L Twin-Turbo I6", 510, 3.5, 290, "RWD / xDrive",
         "Pure track DNA wrapped in a daily-drivable coupe. Razor-sharp steering and a soundtrack that never gets old.",
         [("airline_seat_recline_extra", "M Sport Seats", "Carbon-reinforced bucket seats with full support."),
          ("speed", "M Compound Brakes", "Huge stopping power lap after lap."),
          ("air", "Aero Package", "Carbon roof and active aero elements.")]),

    _car("m3-sedan", "BMW M3 Sedan", 469000, 2025, "Sedan",
         "3.0L Twin-Turbo I6", 480, 3.9, 290, "RWD / xDrive",
         "Four doors, supercar attitude. The sport sedan benchmark, now even sharper.",
         [("event_seat", "Sport Interior", "Premium leather with M stitching."),
          ("settings", "Adaptive M Suspension", "Switch from comfort to track in a tap."),
          ("surround_sound", "Harman Kardon Audio", "Immersive sound in every seat.")]),

    _car("m8-competition", "BMW M8 Competition", 799000, 2024, "Coupe",
         "4.4L V8 Twin-Turbo", 625, 3.2, 305, "xDrive",
         "The flagship of the M family. Grand touring luxury with brutal V8 performance.",
         [("workspace_premium", "Merino Leather", "Handcrafted full-grain interior."),
          ("speed", "Carbon Ceramic Brakes", "Optional brakes built for extremes."),
          ("auto_awesome", "Laserlight Headlights", "Night vision-level visibility.")]),

    _car("x5-m", "BMW X5 M Competition", 659000, 2025, "SUV",
         "4.4L V8 Twin-Turbo", 625, 3.8, 290, "xDrive",
         "A family SUV that refuses to behave like one. Space for five, power for ten.",
         [("family_restroom", "Spacious Cabin", "Comfort for the whole family."),
          ("landscape", "Adaptive Air Suspension", "Smooth on road, ready off it."),
          ("devices", "Curved Display", "Latest BMW iDrive experience.")]),

    _car("i4-m50", "BMW i4 M50", 379000, 2025, "Electric",
         "Dual Electric Motor", 544, 3.9, 225, "xDrive",
         "Electric power with the BMW feel. Silent, instant and seriously quick.",
         [("bolt", "Fast Charging", "10-80% in about 30 minutes."),
          ("battery_charging_full", "Long Range", "Up to 510 km WLTP."),
          ("eco", "Zero Emissions", "Performance with a clean conscience.")]),

    _car("z4-m40i", "BMW Z4 M40i", 329000, 2024, "Coupe",
         "3.0L Turbo I6", 382, 4.5, 250, "RWD",
         "Roof down, windows down. A pure roadster made for open highways.",
         [("wb_sunny", "Soft-top Roof", "Opens or closes in 10 seconds."),
          ("sports_score", "Sport Differential", "Sharp, playful handling."),
          ("speaker", "Premium Sound", "Built for sunset drives.")]),
]