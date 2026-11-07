from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='cars'),
    path('cars/<slug:slug>/', views.car_detail, name='car_detail'),
    path('about/', views.about, name='about'),
]