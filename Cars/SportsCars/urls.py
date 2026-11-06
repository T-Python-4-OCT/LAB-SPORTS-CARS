from . import views
from django.urls import path

app_name = "SportsCars"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("About/", views.about_view, name="about"),
    path("AllCars/", views.all_cars, name="all_cars"),
    path("Porsche/", views.porsche_view, name="porsche"),
    path("Ferrari/", views.ferrari_view, name="ferrari"),
    path("Lamborghini/", views.lamborghini_view, name="lamborghini"),
    path("Contact/", views.contact_view, name="contact"),
    path("dark-mode/", views.dark_mode, name="dark_mode"),
]