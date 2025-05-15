from django.urls import path
from . import views

urlpatterns = [
    path('peticiones', views.peticiones, name='peticiones'),
]         
