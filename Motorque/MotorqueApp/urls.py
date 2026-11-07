
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('cars/', views.all_cars, name='all_cars'),

    # Genesis G80
    path('cars/genesis-g80/', views.genesis_g80, name='genesis_g80'),

    # Porsche 911 Carrera
    path('cars/porsche-911/', views.porsche_911, name='porsche_911'),

    # Cadillac Escalade
    path('cars/cadillac-escalade/', views.cadillac_escalade, name='cadillac_escalade'),
]
