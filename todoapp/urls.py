from django.urls import path
from .views import crear_tarea

urlpatterns = [
    path('crear/', crear_tarea, name='crear_tarea'),
]
