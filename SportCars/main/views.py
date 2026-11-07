
from django.http import Http404
from django.shortcuts import render

CARS = [
    {
        'slug': 'nissan-gt-r', 'name': 'Nissan GT-R', 'brand': 'Nissan',
        'price': 650000, 'year': 2023, 'image': 'gtr.jpg',
        'detail_image': 'gtr-detail.jpg',
        'interior_image': 'gtr-interior.jpg',
        'engine': '3.8 L', 'engine_type': 'Twin-Turbo V6', 'power': '565 hp',
        'acceleration': '3.0 s', 'top_speed': '315 km/h',
        'headline': 'The Legend Known as Godzilla',
        'description': 'Hand-built power and intelligent all-wheel drive '
                       'make the GT-R one of the most capable sports cars on any road.',
    },
    {
        'slug': 'chevrolet-corvette-stingray', 'name': 'Chevrolet Corvette Stingray', 'brand': 'Chevrolet',
        'price': 520000, 'year': 2024, 'image': 'corvette.jpg',
        'detail_image': 'corvette-detail.jpg',
        'interior_image': 'corvette-interior.jpg',
        'engine': '6.2 L', 'engine_type': 'V8', 'power': '495 hp',
        'acceleration': '3.0 s', 'top_speed': '312 km/h',
        'headline': 'America Moves the Engine',
        'description': 'A mid-engine layout and a thunderous V8 give the Corvette '
                       'the balance of a supercar and the comfort of a daily driver.',
    },
    {
        'slug': 'audi-r8', 'name': 'Audi R8 V10', 'brand': 'Audi',
        'price': 890000, 'year': 2023, 'image': 'r8.jpg',
        'detail_image': 'r8-detail.jpg',
        'interior_image': 'r8-interior.jpg',
        'engine': '5.2 L', 'engine_type': 'V10', 'power': '602 hp',
        'acceleration': '3.1 s', 'top_speed': '330 km/h',
        'headline': 'A Supercar for Every Day',
        'description': 'A naturally aspirated V10 and Audi precision combine '
                       'to create a supercar that is thrilling and easy to live with.',
    },
    {
        'slug': 'bmw-m4-competition', 'name': 'BMW M4 Competition', 'brand': 'BMW',
        'price': 560000, 'year': 2024, 'image': 'm4.jpg',
        'detail_image': 'm4-detail.jpg',
        'interior_image': 'm4-interior.jpg',
        'engine': '3.0 L', 'engine_type': 'Twin-Turbo I6', 'power': '503 hp',
        'acceleration': '3.9 s', 'top_speed': '290 km/h',
        'headline': 'Born on the Track',
        'description': 'Sharp steering and a powerful straight-six turn the M4 '
                       'into a true driver\'s car, on the circuit or the commute.',
    },
    {
        'slug': 'ford-mustang-gt', 'name': 'Ford Mustang GT', 'brand': 'Ford',
        'price': 340000, 'year': 2024, 'image': 'mustang.jpg',
        'detail_image': 'mustang-detail.jpg',
        'interior_image': 'mustang-interior.jpg',
        'engine': '5.0 L', 'engine_type': 'V8', 'power': '480 hp',
        'acceleration': '4.3 s', 'top_speed': '250 km/h',
        'headline': 'The Original Muscle Icon',
        'description': 'Classic looks and a naturally aspirated V8 keep '
                       'the Mustang one of the most loved performance cars in the world.',
    },
    {
        'slug': 'toyota-gr-supra', 'name': 'Toyota GR Supra', 'brand': 'Toyota',
        'price': 310000, 'year': 2024, 'image': 'supra.jpg',
        'detail_image': 'supra-detail.jpg',
        'interior_image': 'supra-interior.jpg',
        'engine': '3.0 L', 'engine_type': 'Turbo I6', 'power': '382 hp',
        'acceleration': '4.1 s', 'top_speed': '250 km/h',
        'headline': 'A Japanese Icon Returns',
        'description': 'Compact, light and quick to respond, the GR Supra '
                       'brings a legendary name back to the modern road.',
    },
]


def home(request):
    return render(request, 'main/home.html', {'cars': CARS[:3], 'active': 'home'})


def all_cars(request):
    brands = sorted({car['brand'] for car in CARS})
    years = sorted({car['year'] for car in CARS}, reverse=True)
    context = {'cars': CARS, 'brands': brands, 'years': years, 'active': 'cars'}
    return render(request, 'main/all_cars.html', context)


def car_detail(request, slug):
    for car in CARS:
        if car['slug'] == slug:
            return render(request, 'main/car_detail.html', {'car': car, 'active': 'cars'})
    raise Http404('Car not found')


def about(request):
    return render(request, 'main/about.html', {'active': 'about'})