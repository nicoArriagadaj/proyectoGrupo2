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