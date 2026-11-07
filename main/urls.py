from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.all_cars, name='all_cars'),
    path('cars/bmw-m4/', views.bmw_m4, name='bmw_m4'),
    path('cars/bmw-m3/', views.bmw_m3, name='bmw_m3'),
    path('cars/bmw-m8/', views.bmw_m8, name='bmw_m8'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
