from django.urls import path
from . import views
from .dashboard import dashboard, manage_inquiries, update_inquiry_status
from .car_management import manage_cars, add_car, edit_car
from django.contrib.auth.views import LogoutView
app_name = "cars"


urlpatterns = [
    path("", views.home, name="home"),
    path("cars/", views.all_cars, name="all_cars"),
    path("cars/<int:car_id>/", views.car_detail, name="car_detail"),
    path("compare/",views.compare_cars, name="compare_cars"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("about/", views.about, name="about"),
    path("dashboard/",dashboard, name="dashboard"),
    path("dashboard/inquiries/", manage_inquiries, name="manage_inquiries"),
    path("dashboard/inquiries/<int:inquiry_id>/status/", update_inquiry_status, name="update_inquiry_status"),
    path("dashboard/cars/add/", add_car, name="add_car"),
    path("dashboard/cars/<int:car_id>/edit/", edit_car, name="edit_car"),
    path("dashboard/cars/", manage_cars, name="manage_cars"),
    path("logout/", LogoutView.as_view(next_page="cars:home"), name="admin_logout"),
]
