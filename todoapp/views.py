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
    libros_db = Item.objects.filter(tipo='Libro')
    if request.method  == 'GET':
        return render(request, 'todoapp/view_libros_list.html', {"libros": libros_db})
    else:
        return ""
    
def view_mangas_list(request):
    mangas_db = Item.objects.filter(tipo='Manga')
    if request.method  == 'GET':
        return render(request, 'todoapp/view_mangas_list.html', {"mangas": mangas_db})
    else:
        return ""

def view_animes_list(request):
    animes_db = Item.objects.filter(tipo='Anime')
    if request.method  == 'GET':
        return render(request, 'todoapp/view_animes_list.html', {"animes": animes_db})
    else:
        return ""

def view_peliculas_list(request):
    peliculas_db = Item.objects.filter(tipo='Película')
    if request.method  == 'GET':
        return render(request, 'todoapp/view_peliculas_list.html', {"peliculas": peliculas_db})
    else:
        return ""
    
def view_comics_list(request):
    comics_db = Item.objects.filter(tipo='Cómic')
    if request.method  == 'GET':
        return render(request, 'todoapp/view_comics_list.html', {"comics": comics_db})
    else:
        return ""


