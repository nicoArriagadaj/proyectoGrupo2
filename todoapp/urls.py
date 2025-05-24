from django.urls import path
from todoapp import views

urlpatterns = [
    path('crear/', views.crear_tarea, name='crear_tarea'),  
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),  
]
