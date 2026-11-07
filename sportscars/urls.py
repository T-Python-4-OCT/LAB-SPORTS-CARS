from django.urls import path
from cars import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cars/", views.all_cars, name="cars"),
    path("about/", views.about, name="about"),
    path("cars/<slug:slug>/", views.car_detail, name="car_detail"),
]
