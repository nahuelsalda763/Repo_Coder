from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import Familia
from datetime import date, datetime
from mi_app.models import Curso, Estudiante

from mi_app.forms import CursoBusquedaFormulario, CursoFomulario


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")


def saludo_personalizado(request):
    pass

def mostrar_index(request):
    return render(request, "mi_app/index.html", {"mi_titulo": "Hola este es mi primer website!!!"})

def listar_cursos(request): # vista
    context = {}
    context["cursosssssss"] = Curso.objects.all() # modelo
    return render(request, "mi_app/lista_cursos.html", context) # template


def listar_estudiantes(request):
    context = {}
    context["estudiantes"] = Estudiante.objects.all()
    return render(request, "mi_app/lista_estudiantes.html", context)


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

def formulario_curso(request):
    if request.method == 'POST':
        pass
    else:
        mi_formulario = CursoFomulario()
        return render(request, "mi_app/curso_formulario.html",{"mi_formulario":mi_formulario})


def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()

    if request.GET:
        

        criterio = busqueda_formulario.cleaned_data

        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()

        return render(request, "mi_app/busqueda_curso.html", {"cursos": cursos})

    busqueda_formulario = CursoBusquedaFormulario()

    return render(request, "mi_app/busqueda_curso.html", {"busqueda_formulario": busqueda_formulario })

