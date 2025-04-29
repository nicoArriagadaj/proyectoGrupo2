from django.shortcuts import render, redirect
from .forms import TareaForm
from categorias.models import *

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

def view_libros_list(request):
    libros_db = Libro_test.objects.all()
    if not libros_db.exists():
        print("ASd")
    for libro in libros_db:
        print(libro.titulo)
    if request.method  == 'GET':
        return render(request, 'todoapp/view_libros_list.html', {"libros": libros_db})
    else:
        return ""
    
def view_mangas_list(request):
    if request.method  == 'GET':
        return render(request, 'todoapp/view_mangas_list.html')
    else:
        return ""

def view_animes_list(request):
    if request.method  == 'GET':
        return render(request, 'todoapp/view_animes_list.html')
    else:
        return ""

def view_peliculas_list(request):
    if request.method  == 'GET':
        return render(request, 'todoapp/view_peliculas_list.html')
    else:
        return ""
    
def view_comics_list(request):
    if request.method  == 'GET':
        return render(request, 'todoapp/view_comics_list.html')
    else:
        return ""


