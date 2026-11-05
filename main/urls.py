from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cars/", views.all_cars, name="all_cars"),
    path("cars/<int:car_id>/", views.car_detail, name="car_detail"),
    path("about/", views.about, name="about"),
]