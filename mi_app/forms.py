from django import forms


class CursoFomulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()
    
class CursoBusquedaFormulario(forms.Form):

    criterio = forms.CharField()
    