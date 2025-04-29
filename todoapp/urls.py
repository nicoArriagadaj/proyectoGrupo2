from django.urls import path
from .views import *

urlpatterns = [
    path('crear/', crear_tarea, name='crear_tarea'),
    path('libros/', view_libros_list, name='view_libros_list'),
    path('mangas/', view_mangas_list, name='view_mangas_list'),
    path('animes/', view_animes_list, name='view_animes_list'),
    path('peliculas/', view_peliculas_list, name='view_peliculas_list'),
    path('comics/', view_comics_list, name='view_comics_list'),
]
