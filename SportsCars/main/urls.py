from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cars/', views.all_cars, name='cars'),
    path('cars/<slug:slug>/', views.car_detail, name='car_detail'),
    path('about/', views.about, name='about'),
    path('body-dark/', views.body_dark, name='body_dark'),
]