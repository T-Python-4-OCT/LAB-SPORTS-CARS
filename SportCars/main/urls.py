from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("cars/", views.cars_view, name="cars_view"),
    path("cars/<slug:car_slug>/", views.car_detail_view, name="car_detail_view"),
    path("about/", views.about_view, name="about_view"),

    # Preferences saved in cookies
    path("mode/<str:mode>/", views.mode_view, name="mode_view"),
    path("wishlist/<slug:car_slug>/", views.wishlist_view, name="wishlist_view"),
    path("rate/<slug:car_slug>/<int:stars>/", views.rate_view, name="rate_view"),
    path("forget-me/", views.forget_me_view, name="forget_me_view"),
]
