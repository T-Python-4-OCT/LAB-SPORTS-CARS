from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def all_cars(request):
    return render(request, 'main/all_cars.html')

def bmw_m4(request):
    context = {
        'car_name': 'BMW M4 Competition',
        'car_price': '425,000',
        'car_image': 'main/images/bmw-m4.jpg',
        'car_description': 'Experience the perfect balance of luxury, precision, and outstanding performance with the BMW M4 Competition.',
        'car_power': '510 hp',
        'car_acceleration': '3.9 sec',
        'car_engine': '3.0L',
        'car_speed': '250 km/h',
        'car_body': '2-Door Coupe',
    }

    return render(request, 'main/car_detail.html', context)

def bmw_m3(request):
    context = {
        'car_name': 'BMW M3 Competition',
        'car_price': '380,000',
        'car_image': 'main/images/bmw-m3.jpg',
        'car_description': 'Experience exceptional performance and luxury with the BMW M3 Competition.',
        'car_power': '510 hp',
        'car_acceleration': '3.9 sec',
        'car_engine': '3.0L',
        'car_speed': '250 km/h',
        'car_body': '4-Door Sedan',
    }

    return render(request, 'main/car_detail.html', context)

def bmw_m8(request):
    context = {
        'car_name': 'BMW M8 Competition',
        'car_price': '715,000',
        'car_image': 'main/images/bmw-m8.jpg',
        'car_description': 'Experience exceptional luxury and V8 performance with the BMW M8 Competition.',
        'car_power': '625 hp',
        'car_acceleration': '3.2 sec',
        'car_engine': '4.4L V8',
        'car_speed': '250 km/h',
        'car_body': '2-Door Coupe',
    }

    return render(request, 'main/car_detail.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')