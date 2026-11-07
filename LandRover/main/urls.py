from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("cars/", views.all_cars_view, name="all_cars_view"),
    path("about/", views.about_view, name="about_view"),
    path("cars/range-rover/", views.range_rover_view, name="range_rover_view"),
    path("cars/defender/", views.defender_view, name="defender_view"),
    path("cars/discovery/", views.discovery_view, name="discovery_view"),
    path("toggle-theme/", views.toggle_theme_view, name="toggle_theme_view"),
]