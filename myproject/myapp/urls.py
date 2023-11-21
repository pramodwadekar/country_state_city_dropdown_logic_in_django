from django.contrib import admin
from django.urls import path, include
from .import views
from .views import controls, get_states, get_cities

urlpatterns = [
    path('', controls, name='controls'),
    path("data/", views.data, name = "data"),
    path('get_states/', get_states, name='get_states'),
    path('get_cities/', get_cities, name='get_cities'),
    path("add_data/", views.add_data, name = 'add_data'),
    path("show_data/", views.show_data, name = 'show_data')
]