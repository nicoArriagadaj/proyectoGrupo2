from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Usuario personalizado (opcional)
# la tabla de usuario ya está integrada por Django, pero podemos añadirle más cositas
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username

    
# Modelo general de "Item" (libros, animes, mangas, películas, cómics)
class Item(models.Model):
    TIPO_CHOICES = [
        ('Libro', 'Libro'),
        ('Manga', 'Manga'),
        ('Anime', 'Anime'),
        ('Película', 'Película'),
        ('Cómic', 'Cómic'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    autor = models.CharField(max_length=100, null=True, blank=True)
    estudio = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    editorial = models.CharField(max_length=100, null=True, blank=True)
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    imagen = models.URLField(blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"

