from django.contrib import admin
from .models import Categoria, Receta, Comentario, Bebida, Tip

admin.site.register(Categoria)
admin.site.register(Receta)
admin.site.register(Comentario)
admin.site.register(Bebida)
admin.site.register(Tip)
