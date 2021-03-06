"""mi_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from manejador_contenido.views import mostrar_home, mostrar_profile
from mi_app.views import mis_familiares, listar_estudiantes, listar_cursos


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),
    path('home/', mostrar_home),
    path('profile/', mostrar_profile),
    path('familia/', mis_familiares),
    path('lista_cursos/',listar_cursos),
    path('lista_estudiantes/',listar_estudiantes),
     
]
