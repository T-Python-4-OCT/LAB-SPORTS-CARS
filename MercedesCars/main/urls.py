from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.all_cars, name='all_cars'),
    path('about/', views.about, name='about'),

    path('cars/amg-gt/', views.amg_gt, name='amg_gt'),
    path('cars/c63/', views.c63, name='c63'),
    path('cars/sl63/', views.sl63, name='sl63'),
]