from django.urls import path
from . import views

app_name = "cars"
urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.all_cars, name='all_cars'),
    path('cars/<slug:car_slug>/', views.car_detail, name='car_detail'),
    path('about/', views.about, name='about'),
    path('theme/<str:theme>/', views.set_theme, name='set_theme'),
]