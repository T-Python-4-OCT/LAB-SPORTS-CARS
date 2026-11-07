from django.urls import path

from . import views

app_name = "all_cars"

urlpatterns = [
    path("", views.all_cars, name="index"),
]