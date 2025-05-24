from django.shortcuts import render, redirect
from .forms import TareaForm
from .models import Tarea

def crear_tarea(request):
    # post = Envía información al servidor, cuando usuario hace guardar, hace post a http...
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            # donde lo redirigimos
            return redirect('crear_tarea')
    else:  #GET = Pide información. (cuando ingresamos, hace Get a http.. )
        form = TareaForm()
    return render(request, 'todoapp/crear_tarea.html', {'form': form})

def lista_usuarios(request):
    tareas = Tarea.objects.all()
    return render(request, 'todoapp/lista_usuarios.html', {'tareas': tareas})


