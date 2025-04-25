from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from categorias.models import Categoria

class Tarea(models.Model):  # Todolist able name that inherits models.Model
    titulo = models.CharField(max_length=250)  # un varchar
    contenido = models.TextField(blank=True)  # un text
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # un date
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)



    def __str__(self):
        return self.titulo  # name to be shown when called