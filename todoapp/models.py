from django.db import models
#from categorias.models import Categoria  

class Tarea(models.Model):
    Nombre = models.CharField(max_length=100)
    Username = models.CharField(max_length=150)
    Contraseña = models.CharField(max_length=128)  
    Correo = models.EmailField(max_length=254)  

    def __str__(self):
        return self.Nombre
