from django import forms
from .models import Receta, Comentario,  Bebida, Tip

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'preparacion', 'imagen', 'categoria']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['titulo', 'descripcion', 'categoria', 'imagen']  

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['titulo', 'contenido', 'categoria']  