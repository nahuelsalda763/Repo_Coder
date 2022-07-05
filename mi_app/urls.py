from django.urls import path
from mi_app import views
from mi_app.views import mis_familiares

urlpatterns = [

    path('',views.inicio),
    path("mi-pagina/", views.mostrar_index),
    path("mi-familia/", views.mis_familiares),

]