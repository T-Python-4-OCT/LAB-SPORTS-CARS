from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('mode/<mode>/', views.mode_view, name='mode_view'),
    path('cars/', views.cars_view, name='cars'),
    path('cars/<int:car_id>/', views.car_detail_view, name='car_detail'),
    path('about/', views.about_view, name='about'),
]