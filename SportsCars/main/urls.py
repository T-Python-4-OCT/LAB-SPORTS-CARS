from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("cars/", views.cars_view, name="cars"),
    path("cars/<slug:slug>/", views.car_detail_view, name="car_detail"),
    path("about/", views.about_view, name="about"),
    path("mode/<str:mode>/", views.mode_view, name="mode"),
    path("lang/<str:lang>/", views.lang_view, name="lang"),
]

#mohammad Alnsafi