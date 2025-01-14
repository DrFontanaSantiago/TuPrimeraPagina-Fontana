from django import forms
from .models import Receta, Comentario

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'preparacion', 'imagen', 'categoria']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']