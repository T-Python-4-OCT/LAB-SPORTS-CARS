# main/data.py
# Car data in English, with an "ar" copy for Arabic

CARS = [
    {
        "slug": "range-rover-sport-autobiography",
        "name": "Range Rover Sport Autobiography",
        "tagline": "Peak luxury meets sporting performance",
        "description": "Available as Petrol, Plug-In Hybrid or Electric. Adds Digital LED headlights with signature DRL and Image Projection, plus 22-way heated and ventilated massage front seats.",
        "price": 791808,
        "price_label": "From SAR 791,808",
        "year": 2026,
        "image": "images/range-rover-1.jpg",
        "gallery": [
            "images/range-rover-1.jpg",
            "images/range-rover-2.jpg",
            "images/range-rover-3.jpg",
            "images/range-rover-4.jpg",
        ],
        "specs": [
            {"icon": "bolt", "label": "Power", "value": "394 hp"},
            {"icon": "timer", "label": "0-100 km/h", "value": "5.7 s"},
            {"icon": "speed", "label": "Top Speed", "value": "242 km/h"},
            {"icon": "airline_seat_recline_extra", "label": "Seats", "value": "5"},
        ],
        "ar": {
            "name": "رينج روڤر سبورت أوتوبيوغرافي",
            "tagline": "فخامة القمة بروح رياضية",
            "description": "متوفرة بمحرك بنزين أو هايبرد قابل للشحن أو كهربائي. تضيف مصابيح LED رقمية بإضاءة نهارية مميزة وخاصية عرض الصور، ومقاعد أمامية بـ 22 وضعية مع تدفئة وتهوية وتدليك.",
            "price_label": "يبدأ من 791,808 ريال",
            "specs": [
                {"icon": "bolt", "label": "القوة", "value": "394 حصان"},
                {"icon": "timer", "label": "التسارع من 0 إلى 100", "value": "5.7 ثانية"},
                {"icon": "speed", "label": "السرعة القصوى", "value": "242 كم/س"},
                {"icon": "airline_seat_recline_extra", "label": "المقاعد", "value": "5"},
            ],
        },
    },
    {
        "slug": "range-rover-sv-black",
        "name": "Range Rover SV Black",
        "tagline": "The all-black flagship",
        "description": "Range Rover Autobiography features, plus 23-inch forged wheels, SV Gloss Black Exterior Pack, 24-way hot stone massage front seats and Executive Class Comfort Plus rear seats. Available as Petrol or Electric.",
        "price": 1147400,
        "price_label": "From SAR 1,147,400",
        "year": 2026,
        "image": "images/range-rover-sport-1.jpg",
        "gallery": [
            "images/range-rover-sport-1.jpg",
            "images/range-rover-sport-2.jpg",
            "images/range-rover-sport-3.jpg",
            "images/range-rover-sport-4.jpg",
        ],
        "specs": [
            {"icon": "bolt", "label": "Power", "value": "615 hp"},
            {"icon": "timer", "label": "0-100 km/h", "value": "4.5 s"},
            {"icon": "speed", "label": "Top Speed", "value": "261 km/h"},
            {"icon": "settings", "label": "Torque", "value": "750 Nm"},
        ],
        "ar": {
            "name": "رينج روڤر SV بلاك",
            "tagline": "قمة الفخامة بالأسود الكامل",
            "description": "كل مزايا رينج روڤر أوتوبيوغرافي، مع جنوط مطروقة مقاس 23 بوصة، وحزمة SV السوداء اللامعة للهيكل، ومقاعد أمامية بـ 24 وضعية مع تدليك بالأحجار الدافئة، ومقاعد خلفية فاخرة لرجال الأعمال. متوفرة بمحرك بنزين أو كهربائي.",
            "price_label": "يبدأ من 1,147,400 ريال",
            "specs": [
                {"icon": "bolt", "label": "القوة", "value": "615 حصان"},
                {"icon": "timer", "label": "التسارع من 0 إلى 100", "value": "4.5 ثانية"},
                {"icon": "speed", "label": "السرعة القصوى", "value": "261 كم/س"},
                {"icon": "settings", "label": "عزم الدوران", "value": "750 نيوتن متر"},
            ],
        },
    },
    {
        "slug": "defender-110-x-dynamic-hse",
        "name": "Defender 110 X-Dynamic HSE",
        "tagline": "Unstoppable. Anywhere.",
        "description": "P400 Petrol Mild Hybrid in Fuji White with Caraway/Ebony interior. Includes Off-Road Pack, 3D Surround Camera, Matrix LED headlights and 14-way heated and cooled memory front seats. 5-year / 150,000 km warranty.",
        "price": 466814,
        "price_label": "SAR 466,814",
        "year": 2026,
        "image": "images/defender-1.jpg",
        "gallery": [
            "images/defender-1.jpg",
            "images/defender-2.jpg",
            "images/defender-3.jpg",
            "images/defender-4.jpg",
        ],
        "specs": [
            {"icon": "bolt", "label": "Power", "value": "394 hp"},
            {"icon": "timer", "label": "0-100 km/h", "value": "6.1 s"},
            {"icon": "speed", "label": "Top Speed", "value": "191 km/h"},
            {"icon": "airline_seat_recline_extra", "label": "Seats", "value": "5"},
        ],
        "ar": {
            "name": "ديفندر 110 X-Dynamic HSE",
            "tagline": "لا يُقهر، في أي مكان",
            "description": "محرك P400 بنزين هايبرد خفيف، بلون أبيض فوجي ومقصورة Caraway/Ebony. يشمل حزمة الطرق الوعرة، وكاميرا محيطية ثلاثية الأبعاد، ومصابيح Matrix LED، ومقاعد أمامية بـ 14 وضعية مع تدفئة وتبريد وذاكرة. ضمان 5 سنوات أو 150,000 كم.",
            "price_label": "466,814 ريال",
            "specs": [
                {"icon": "bolt", "label": "القوة", "value": "394 حصان"},
                {"icon": "timer", "label": "التسارع من 0 إلى 100", "value": "6.1 ثانية"},
                {"icon": "speed", "label": "السرعة القصوى", "value": "191 كم/س"},
                {"icon": "airline_seat_recline_extra", "label": "المقاعد", "value": "5"},
            ],
        },
    },
]

# mohammad Alnsafi