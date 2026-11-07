from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("cars/", views.all_cars_view, name="all_cars"),
    path("cars/<slug:slug>/", views.car_detail_view, name="car_detail"),
    path("about/", views.about_view, name="about"),
    path("theme/", views.toggle_theme_view, name="toggle_theme"),
]
