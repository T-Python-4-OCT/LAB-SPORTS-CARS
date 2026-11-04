from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest
from django.utils.http import url_has_allowed_host_and_scheme


def home(request: HttpRequest):
    return render(request, 'home.html')


def all_cars(request: HttpRequest):
    return render(request, 'all_cars.html')


def car_detail(request: HttpRequest, car_slug):
    return render(request, 'car_detail.html', {'car_slug': car_slug})


def about(request: HttpRequest):
    return render(request, 'about.html')


def set_theme(request: HttpRequest, theme):
    # نقبل قيمتين فقط، وأي قيمة غيرها نعتبرها light
    if theme not in ('light', 'dark'):
        theme = 'light'

    # الصفحة التي نرجع لها بعد تغيير الوضع (تأتي من ?next= في الرابط)
    next_url = request.GET.get('next')

    # نتأكد أن رابط العودة داخل موقعنا فقط، وإلا نرجع للرئيسية
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = resolve_url('home')

    response = redirect(next_url)
    # نحفظ الاختيار في Cookie لمدة سنة
    response.set_cookie('site_theme', theme, max_age=60 * 60 * 24 * 365)
    return response