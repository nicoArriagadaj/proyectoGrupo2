from django.shortcuts import render, redirect
from .forms import TareaForm

def crear_tarea(request):
    # post = Envía información al servidor, cuando usuario hace guardar, hace post a http...
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio') 
    else:  #GET = Pide información. (cuando ingresamos, hace Get a http.. )
        form = TareaForm()
    return render(request, 'todoapp/crear_tarea.html', {'form': form})

# Create your views here.

