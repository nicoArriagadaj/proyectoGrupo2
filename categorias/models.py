from django.db import models
"""" 
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    """
# Un test simple para mostrar atributos básicos, despues usaré la definida
# Para insertar facil a la base de datos:

# py manage.py shell
# >> from categorias.models import Libro_test
# >> Libro_test.objects.create(titulo="<nombre_libro>")
# >> quit()

class Libro_test(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):       
        return self.titulo
    
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
