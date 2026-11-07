def image(name, alt):
    return {"path": f"images/{name}.webp", "alt": alt}


VEHICLES = [
    {
        "slug": "hyundai-genesis-coupe", "url_name": "genesis", "brand": "Hyundai",
        "name": "Hyundai Genesis Coupe", "model": "Genesis Coupe", "year": 2013,
        "demo_price_sar": 65000,
        "engine": "3.8L V6", "displacement": "3.8 L", "engine_label": "Naturally Aspirated",
        "power": "348 hp", "transmission": "6-speed manual", "drive": "Rear-wheel drive",
        "overview_title": "The Spirit of the Sports Coupe",
        "overview": "A naturally aspirated V6, rear-wheel drive, and a six-speed manual define this Genesis Coupe. Its two-door profile puts the driving experience first.",
        "reference_note": "2013 US-market 3.8 R-Spec specifications. Professional model-reference photos; equipment may differ from individual vehicles.",
        "gallery": [
            image("editorial/genesis-architecture", "Dark Hyundai Genesis Coupe on a wet architectural plaza"),
            image("editorial/genesis-motion", "Dark Hyundai Genesis Coupe driving past a modern building at dusk"),
            image("editorial/genesis-front-motion", "Dark Hyundai Genesis Coupe driving through a modern covered urban passage"),
            image("editorial/genesis-rear-architecture", "Dark Hyundai Genesis Coupe rear three-quarter view on a wet architectural plaza"),
            image("editorial/genesis-manual-cockpit", "Hyundai Genesis Coupe driver cockpit with a six-speed manual gear lever and three pedals"),
        ],
        "features": [
            {"title": "3.8 GDI V6", "description": "A naturally aspirated 3.8-litre V6 delivers 348 hp to the rear wheels.", "image": image("editorial/genesis-v6-engine", "Hyundai Genesis Coupe 3.8 GDI V6 engine bay")},
            {"title": "Six-Speed Manual", "description": "A six-speed manual puts every gear change in your hands.", "image": image("editorial/genesis-manual-shifter", "Hyundai Genesis Coupe six-speed manual shifter and center-console detail")},
            {"title": "Classic Coupe Proportions", "description": "A low roofline, sculpted rear quarters, and a purposeful two-door silhouette.", "image": image("editorial/genesis-rear-architecture", "Dark Hyundai Genesis Coupe rear three-quarter view on a wet architectural plaza")},
        ],
    },
    {
        "slug": "hyundai-elantra-n-2025", "url_name": "elantra", "brand": "Hyundai",
        "name": "Hyundai Elantra N 2025", "model": "Elantra N", "year": 2025,
        "exterior_color": "Performance Blue",
        "demo_price_sar": 125000,
        "engine": "2.0L Turbo GDI", "displacement": "2.0 L", "engine_label": "Turbocharged",
        "power": "276 hp", "transmission": "6-speed manual", "drive": "Front-wheel drive",
        "overview_title": "Performance Blue. Pure N.",
        "overview": "Performance Blue paint, red lower accents, and a black rear wing give the Elantra N its unmistakable presence. A 276-hp turbocharged engine, six-speed manual, and electronic limited-slip differential put the driver at the heart of every corner.",
        "reference_note": "2025 US-market Elantra N six-speed manual specifications in Performance Blue. Official Hyundai model-reference photography; some campaign images may show optional equipment. Demo price is illustrative.",
        "overview_image": image("editorial/elantra-n-2025-architecture", "Performance Blue Hyundai Elantra N parked outside a modern brick building"),
        "gallery": [
            image("editorial/elantra-n-2025-driving", "Performance Blue Hyundai Elantra N driving around a forest-road curve"),
            image("editorial/elantra-n-2025-rear", "Performance Blue Hyundai Elantra N rear view with black wing and twin exhausts"),
            image("editorial/elantra-n-2025-front", "Close-up of the Performance Blue Hyundai Elantra N front fascia and red lower trim"),
            image("editorial/elantra-n-2025-profile", "2025 Hyundai Elantra N six-speed manual in Performance Blue, exact side-profile reference"),
        ],
        "features": [
            {"title": "19-inch Alloy Wheels", "description": "N alloy wheels, Michelin Pilot Sport 4S tires, and red brake calipers.", "image": image("editorial/elantra-n-2025-wheel", "Hyundai Elantra N 19-inch alloy wheel and red N brake caliper beside Performance Blue bodywork")},
            {"title": "Signature N Design", "description": "A bold front fascia, Performance Blue bodywork, and signature red lower accents.", "image": image("editorial/elantra-n-2025-front", "Performance Blue Hyundai Elantra N front fascia and red lower trim")},
            {"title": "N Rear Wing", "description": "A black rear wing and twin exhausts complete the N silhouette.", "image": image("editorial/elantra-n-2025-rear", "Performance Blue Hyundai Elantra N rear view with black wing and twin exhausts")},
        ],
    },
    {
        "slug": "hyundai-sonata-n-line", "url_name": "sonata", "brand": "Hyundai",
        "name": "Hyundai Sonata N Line", "model": "Sonata N Line", "year": 2024,
        "demo_price_sar": 165000,
        "engine": "2.5L Turbo GDI", "displacement": "2.5 L", "engine_label": "Turbocharged",
        "power": "290 hp", "transmission": "8-speed wet DCT", "drive": "Front-wheel drive",
        "overview_title": "Space Meets Performance",
        "overview": "The Sonata N Line combines a 2.5-litre turbo engine with an eight-speed wet dual-clutch transmission. A spacious cabin and a distinctive exterior bring comfort and performance together.",
        "reference_note": "International N Line reference specifications and photography. Model year, equipment, and availability vary by market.",
        "gallery": [
            image("editorial/sonata-hangar-front", "Red Hyundai Sonata N Line beside a sunlit aircraft hangar"),
            image("editorial/sonata-hangar-rear", "Red Hyundai Sonata N Line rear three-quarter view in a sunlit hangar"),
            image("editorial/sonata-wheel", "Hyundai Sonata N Line 19-inch alloy wheel and red bodywork detail"),
        ],
        "features": [
            {"title": "19-inch Alloy Wheels", "description": "N Line alloy wheels with a distinctive machined design.", "image": image("editorial/sonata-wheel", "Hyundai Sonata N Line 19-inch alloy wheel and red bodywork detail")},
            {"title": "Turbocharged Power", "description": "A 2.5-litre engine paired with an eight-speed DCT.", "image": image("editorial/sonata-hangar-front", "Red Hyundai Sonata N Line beside a sunlit aircraft hangar")},
            {"title": "N Line Styling", "description": "Distinctive bodywork and a wide front grille.", "image": image("editorial/sonata-grille", "Hyundai Sonata N Line grille and front light detail")},
        ],
    },
]

for vehicle in VEHICLES:
    vehicle["image"] = vehicle["gallery"][0]
    vehicle.setdefault("overview_image", vehicle["gallery"][1])

VEHICLES_BY_SLUG = {vehicle["slug"]: vehicle for vehicle in VEHICLES}
SOCIAL_LINKS = [
    {"name": "Instagram", "url": "https://www.instagram.com/hyundaiwallan/", "icon": "instagram"},
    {"name": "YouTube", "url": "https://www.youtube.com/channel/UC_1hgpyLjqxy5upvvfiOkog", "icon": "youtube"},
    {"name": "Facebook", "url": "https://www.facebook.com/HyundaiSaudiWallan/", "icon": "facebook"},
    {"name": "X", "url": "https://x.com/HyundaiWallan", "icon": "x"},
]
