
from django.http import Http404
from django.shortcuts import render


def home(request):
    return render(request, 'Cars/home.html')


def about(request):
    return render(request, 'Cars/about.html')


def all_cars(request):
    cars = [
        {
            'name': 'Ferrari F8 Tributo',
            'brand': 'Ferrari',
            'model': 'F8 Tributo',
            'year': 2023,
            'price': 1250000,
            'engine': 'V8 Twin Turbo',
            'image': 'https://images.unsplash.com/photo-1592198084033-aade902d1aae?w=800',
            'slug': 'ferrari'
        },
        {
            'name': 'Porsche 911 Turbo S',
            'brand': 'Porsche',
            'model': '911 Turbo S',
            'year': 2024,
            'price': 1295000,
            'engine': '3.8L Twin Turbo',
            'image': 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800',
            'slug': 'porsche'
        },
        {
            'name': 'Lamborghini Huracán',
            'brand': 'Lamborghini',
            'model': 'Huracán',
            'year': 2023,
            'price': 1150000,
            'engine': '5.2L V10',
            'image': 'https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?w=800',
            'slug': 'lamborghini'
        },
        {
            'name': 'McLaren 720S',
            'brand': 'McLaren',
            'model': '720S',
            'year': 2022,
            'price': 1106250,
            'engine': '4.0L V8',
            'image': 'https://images.unsplash.com/photo-1621135802920-133df287f89c?w=800',
            'slug': ''
        },
        {
            'name': 'Aston Martin Vantage',
            'brand': 'Aston Martin',
            'model': 'Vantage',
            'year': 2023,
            'price': 693750,
            'engine': '4.0L V8',
            'image': 'https://images.unsplash.com/photo-1614200187524-dc4b892acf16?w=800',
            'slug': ''
        },
        {
            'name': 'Mercedes-AMG GT R',
            'brand': 'Mercedes-Benz',
            'model': 'AMG GT R',
            'year': 2022,
            'price': 787500,
            'engine': '4.0L V8',
            'image': 'https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=800',
            'slug': ''
        }
    ]

    for car in cars:
        car['price_display'] = f"{car['price']:,}"

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


CARS = {
    'ferrari': {
        'name': 'Ferrari F8 Tributo',
        'brand': 'Ferrari',
        'year': 2023,
        'price': 'SAR 1,250,000',
        'engine': '3.9L Twin-Turbo V8',
        'power': '710 HP',
        'acceleration': '2.9 Seconds',
        'top_speed': '340 km/h',
        'image': 'https://images.unsplash.com/photo-1592198084033-aade902d1aae?w=1200',
        'description': 'The Ferrari F8 Tributo combines exceptional performance, Italian design, and advanced engineering for an unforgettable driving experience.'
    },
    'porsche': {
        'name': 'Porsche 911 Turbo S',
        'brand': 'Porsche',
        'year': 2024,
        'price': 'SAR 1,295,000',
        'engine': '3.8L Twin-Turbo Flat-Six',
        'power': '640 HP',
        'acceleration': '2.7 Seconds',
        'top_speed': '330 km/h',
        'image': 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=1200',
        'description': 'The Porsche 911 Turbo S delivers extraordinary acceleration, precise handling, and everyday comfort.'
    },
    'lamborghini': {
        'name': 'Lamborghini Huracán',
        'brand': 'Lamborghini',
        'year': 2023,
        'price': 'SAR 1,150,000',
        'engine': '5.2L Naturally Aspirated V10',
        'power': '631 HP',
        'acceleration': '2.9 Seconds',
        'top_speed': '325 km/h',
        'image': 'https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?w=1200',
        'description': 'The Lamborghini Huracán offers breathtaking design, thrilling V10 performance, and a truly distinctive driving experience.'
    }
}


def car_detail(request, car_slug):
    car = CARS.get(car_slug)

    if car is None:
        raise Http404("Car not found")

    return render(request, 'Cars/car_detail.html', {'car': car})
