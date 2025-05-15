from django.shortcuts import render, redirect

# Create your views here.
#from peticiones.models import 
#from categorias.models import Item


def peticiones(request): #the index view
    if request.method == "GET":
        return render(request, "peticiones/peticion.html", )
