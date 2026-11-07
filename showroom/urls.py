from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "showroom"
urlpatterns = [
    path("", views.home, name="home"),
    path("cars/", views.cars, name="cars"),
    path("cars/hyundai-genesis-coupe/", views.detail, {"slug": "hyundai-genesis-coupe"}, name="genesis"),
    path("cars/hyundai-elantra-n-2025/", views.detail, {"slug": "hyundai-elantra-n-2025"}, name="elantra"),
    path("cars/hyundai-elantra-n-line-2026/", RedirectView.as_view(pattern_name="showroom:elantra", permanent=True, query_string=True), name="elantra-legacy"),
    path("cars/hyundai-sonata-n-line/", views.detail, {"slug": "hyundai-sonata-n-line"}, name="sonata"),
    path("about/", views.about, name="about"),
]
