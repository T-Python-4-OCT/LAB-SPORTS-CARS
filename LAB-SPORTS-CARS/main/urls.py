from django.urls import path
from django.views.generic import TemplateView
from . import views

def page(template):
    return TemplateView.as_view(template_name=template)

urlpatterns = [
    path("", page("home.html"), name="home"),
    path("cars/", page("cars.html"), name="cars"),
    path("cars/porsche-911-turbo-s/", page("porsche.html"), name="porsche"),
    path("cars/ferrari-f8-tributo/", page("ferrari.html"), name="ferrari"),
    path("cars/lamborghini-huracan/", page("lamborghini.html"), name="lamborghini"),
    path("about/", page("about.html"), name="about"),
    path("theme/", views.toggle_theme, name="toggle_theme"),
]