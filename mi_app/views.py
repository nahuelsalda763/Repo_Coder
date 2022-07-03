from django.shortcuts import render
from django.http import HttpResponse

from mi_app.models import Familia

def inicio(request):
    return HttpResponse("Vista Inicio")

def mostrar_index(request):
    return render(request, "mi_app/index.html",{"mi_titulo":"Mi Aplicacion de CoderHouse"})



def mis_familiares(request):
    context = {
        "Familiares": Familia.objects.all()

    }
    return render (request, "mi_app/mi_familia.html", context)


# Create your views here.
