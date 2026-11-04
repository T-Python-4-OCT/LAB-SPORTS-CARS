from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("cars/", views.cars_view, name="cars_view"),
    path("cars/<int:car_id>/", views.car_detail_view, name="car_detail_view"),
    path("about/", views.about_view, name="about_view"),
]