from django.contrib import admin
from django.urls import path
from mi_app import views
from mi_app.views import formulario_curso, formulario_busqueda
from mi_app.views import (saludar_a, saludo, 
        saludo_personalizado, mostrar_index)


urlpatterns = [
    path('mi-pagina/', mostrar_index),
    path('saludar/persona/<nombre>', saludar_a),
    path('saludo-personalizado/', saludo_personalizado),
    path('formulario/',formulario_curso),
    path('buscar/', formulario_busqueda)
]