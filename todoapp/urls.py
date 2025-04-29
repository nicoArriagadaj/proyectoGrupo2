from django.urls import path
from todoapp import views

urlpatterns = [
    path('crear/',views.crear_tarea),
]
