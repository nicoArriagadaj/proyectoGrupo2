from django.db import models
#from categorias.models import Categoria  

# todos los campos obligatorios por ahora
class Tarea(models.Model):
    Nombre = models.CharField(max_length=100,null=False, blank=False)
    Username = models.CharField(max_length=150,null=False, blank=False)
    Contraseña = models.CharField(max_length=128,null=False, blank=False)  
    Correo = models.EmailField(max_length=254,null=False, blank=False)  

    def __str__(self):
        return self.Nombre
