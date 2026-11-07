from django.urls import path

from . import views

app_name = "car_details"

urlpatterns = [
    path("<slug:slug>/", views.car_detail, name="detail"),
]