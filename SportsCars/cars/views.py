
from django.http import Http404
from django.shortcuts import render


def home(request):
    return render(request, 'Cars/home.html')


def about(request):
    return render(request, 'Cars/about.html')


CARS = {
    'ferrari': {
        'name': 'Ferrari F8 Tributo',
        'brand': 'Ferrari',
        'model': 'F8 Tributo',
        'year': 2023,
        'price': 1250000,
        'engine': '3.9L Twin-Turbo V8',
        'power': '710 HP',
        'acceleration': '2.9 Seconds',
        'top_speed': '340 km/h',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/7/70/Vue_trois_quarts_avant_F8_tributo.jpg',
        'gallery': [
            'https://upload.wikimedia.org/wikipedia/commons/7/70/Vue_trois_quarts_avant_F8_tributo.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/25/Vue_trois_quarts_arri%C3%A8re_F8.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/95/Vue_arri%C3%A8re_Ferrari_F8_tributo.jpg'
        ],
        'description': 'The Ferrari F8 Tributo combines exceptional performance, Italian design, and advanced engineering for an unforgettable driving experience.'
    },
    'porsche': {
        'name': 'Porsche 911 Turbo S',
        'brand': 'Porsche',
        'model': '911 Turbo S',
        'year': 2024,
        'price': 1295000,
        'engine': '3.8L Twin-Turbo Flat-Six',
        'power': '640 HP',
        'acceleration': '2.7 Seconds',
        'top_speed': '330 km/h',
        'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/2023_Porsche_992_Turbo_S_in_Peridot_Metallic%2C_front_left.jpg?width=1200',
        'gallery': [
            'https://commons.wikimedia.org/wiki/Special:FilePath/2023_Porsche_992_Turbo_S_in_Peridot_Metallic%2C_front_left.jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/2023_Porsche_992_Turbo_S_in_Peridot_Metallic%2C_rear_left.jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/2023_Porsche_992_Turbo_S_in_Peridot_Metallic%2C_front_left.jpg?width=800'
        ],
        'description': 'The Porsche 911 Turbo S delivers extraordinary acceleration, precise handling, and everyday comfort.'
    },
    'lamborghini': {
        'name': 'Lamborghini Huracán',
        'brand': 'Lamborghini',
        'model': 'Huracán',
        'year': 2023,
        'price': 1150000,
        'engine': '5.2L Naturally Aspirated V10',
        'power': '631 HP',
        'acceleration': '2.9 Seconds',
        'top_speed': '325 km/h',
        'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/2016_Lamborghini_Hurac%C3%A1n_LP_610-4_Coupe_(1).jpg?width=1200',
        'gallery': [
            'https://commons.wikimedia.org/wiki/Special:FilePath/2016_Lamborghini_Hurac%C3%A1n_LP_610-4_Coupe_(1).jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/2016_Lamborghini_Hurac%C3%A1n_LP_610-4_Coupe_(2).jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/2016_Lamborghini_Hurac%C3%A1n_LP_610-4_Coupe_(interior).jpg?width=1200'
        ],
        'description': 'The Lamborghini Huracán combines striking Italian design with a naturally aspirated V10 engine and thrilling performance.'
    },
    'mclaren': {
        'name': 'McLaren 720S',
        'brand': 'McLaren',
        'model': '720S',
        'year': 2022,
        'price': 1106250,
        'engine': '4.0L Twin-Turbo V8',
        'power': '710 HP',
        'acceleration': '2.9 Seconds',
        'top_speed': '341 km/h',
        'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/McLaren_720S_September_2024_001.jpg?width=1200',
        'gallery': [
            'https://commons.wikimedia.org/wiki/Special:FilePath/McLaren_720S_September_2024_001.jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/McLaren_720S_September_2024_002.jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/McLaren_720S_September_2024_003.jpg?width=1200'
        ],
        'description': 'The McLaren 720S combines lightweight engineering, active aerodynamics, and exceptional twin-turbo V8 performance.'
    },
    'aston-martin': {
        'name': 'Aston Martin Vantage',
        'brand': 'Aston Martin',
        'model': 'Vantage',
        'year': 2023,
        'price': 693750,
        'engine': '4.0L Twin-Turbo V8',
        'power': '503 HP',
        'acceleration': '3.6 Seconds',
        'top_speed': '314 km/h',
        'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/2019_Aston_Martin_Vantage%2C_front_left_view_(Greenwich_2018).jpg?width=1200',
        'gallery': [
            'https://commons.wikimedia.org/wiki/Special:FilePath/2019_Aston_Martin_Vantage%2C_front_left_view_(Greenwich_2018).jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/2019_Aston_Martin_Vantage%2C_front_right_view_(Greenwich_2018).jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/2019_Aston_Martin_Vantage%2C_side_view_(Greenwich_2018).jpg?width=1200'
        ],
        'description': 'The Aston Martin Vantage combines British luxury, elegant styling, and thrilling V8 performance.'
    },
    'mercedes': {
        'name': 'Mercedes-AMG GT R',
        'brand': 'Mercedes-Benz',
        'model': 'AMG GT R',
        'year': 2022,
        'price': 787500,
        'engine': '4.0L Twin-Turbo V8',
        'power': '577 HP',
        'acceleration': '3.6 Seconds',
        'top_speed': '318 km/h',
        'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/Mercedes-AMG_GT_R_(C190)_front.jpg?width=1200',
        'gallery': [
            'https://commons.wikimedia.org/wiki/Special:FilePath/Mercedes-AMG_GT_R_(C190)_front.jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/Mercedes-AMG_GT_R_(C190)_rear.jpg?width=1200',
            'https://commons.wikimedia.org/wiki/Special:FilePath/Mercedes-AMG_GT_R_(C190)_interior.jpg?width=1200'
        ],
        'description': 'The Mercedes-AMG GT R blends motorsport-inspired aerodynamics, bold design, and powerful V8 engineering.'
    }
}


def all_cars(request):
    cars = []

    for slug, car in CARS.items():
        cars.append({
            'name': car['name'],
            'brand': car['brand'],
            'model': car['model'],
            'year': car['year'],
            'price': car['price'],
            'price_display': f"{car['price']:,}",
            'engine': car['engine'],
            'image': car['image'],
            'slug': slug
        })

    brand = request.GET.get('brand', '')
    model = request.GET.get('model', '')
    price = request.GET.get('price', '')
    year = request.GET.get('year', '')

    filtered_cars = cars

    if brand:
        filtered_cars = [
            car for car in filtered_cars
            if car['brand'] == brand
        ]

    if model:
        filtered_cars = [
            car for car in filtered_cars
            if car['model'] == model
        ]

    if price == 'under800':
        filtered_cars = [
            car for car in filtered_cars
            if car['price'] < 800000
        ]
    elif price == '800to1200':
        filtered_cars = [
            car for car in filtered_cars
            if 800000 <= car['price'] <= 1200000
        ]
    elif price == 'above1200':
        filtered_cars = [
            car for car in filtered_cars
            if car['price'] > 1200000
        ]

    if year:
        filtered_cars = [
            car for car in filtered_cars
            if str(car['year']) == year
        ]

    context = {
        'cars': filtered_cars,
        'all_cars': cars,
        'count': len(filtered_cars),
        'selected_brand': brand,
        'selected_model': model,
        'selected_price': price,
        'selected_year': year
    }

    return render(request, 'Cars/all_cars.html', context)


def car_detail(request, car_slug):
    car = CARS.get(car_slug)

    if car is None:
        raise Http404('Car not found')

    car_data = car.copy()
    car_data['price'] = f"SAR {car['price']:,}"

    return render(
        request,
        'Cars/car_detail.html',
        {'car': car_data}
    )
