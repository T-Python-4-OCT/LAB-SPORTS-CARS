from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cars/", views.cars, name="cars"),
    path("cars/<slug:slug>/", views.car_detail, name="car_detail"),
    path("about/", views.about, name="about"),
    path("toggle-theme/", views.toggle_theme, name="toggle_theme"),
]