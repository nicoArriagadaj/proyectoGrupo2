from django import forms
from .models import Tarea

# definimos el formulario, con model = tarea, ya definida en models.py
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['Nombre', 'Username', 'Contraseña', 'Correo']
