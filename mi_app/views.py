from django.shortcuts import render
from django.http import HttpResponse

from mi_app.models import Familia

def mi_template(request):
    return render(request, "mi_app/index.html")

def mis_familiares(request):
    context = {
        "Familiares": Familia.objects.all()

    }
    return render (request, "mi_app/mi_familia.html", context)

# Create your views here.
