from . import views
from django.urls import path

app_name="SportsCars"

urlpatterns=[

    path("",views.home_page,name="home_page"),
    path("Trems/", views.trems_view, name="trems"),

]