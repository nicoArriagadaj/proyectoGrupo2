from django.db import models
from django.utils import timezone
#from categorias.models import Item

class Peticion(models.Model):

    estado_peticion = [
        ("PENDIENTE", "Pendiente"),
        ("ACEPTADO", "Aceptado"),
        ("RECHAZADO", "Rechazado")
    ]

    titulo = models.CharField(max_length=250)  # un varchar
    estado = models.CharField(max_length=9, choices=estado_peticion, default="PENDIENTE")
    #tipo = models.CharField(max_length=20, choices=Item.tipo.choices)
    

    def __str__(self):
        return self.titulo  # name to be shown when called
# Create your models here.
