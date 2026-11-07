from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path("", views.home, name="home"),
    path("cars/", views.all_cars, name="all_cars"),
    path("cars/<slug:slug>/", views.car_detail, name="car_detail"),
    path("about/", views.about, name="about"),
    path("mode/<str:mode>/", views.mode_view, name="mode_view"),
]