from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('all_cars/', views.all_cars, name='all_cars'),
    path('cars/<slug:car_slug>/', views.car_detail, name='car_detail'),
]