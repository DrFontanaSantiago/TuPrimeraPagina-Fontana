from django.urls import path
from . import views
from .views import listar_paginas, detalle_pagina, agregar_pagina, editar_pagina, eliminar_pagina


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recetas/', views.listar_recetas, name='listar_recetas'),  
    path('recetas/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),  
    path('recetas/agregar/', views.agregar_receta, name='agregar_receta'), 
    path('categorias/<slug:slug>/', views.listar_por_categoria, name='listar_por_categoria'),
    path('bebidas/', views.listar_bebidas, name='listar_bebidas'),
    path('bebidas/<int:bebida_id>/', views.detalle_bebida, name='detalle_bebida'),
    path('tips/', views.listar_tips, name='listar_tips'),
    path('tips/<int:tip_id>/', views.detalle_tip, name='detalle_tip'),
    path('exito/', views.exito, name='exito'),
    path('agregar-bebida/', views.agregar_bebida, name='agregar_bebida'),
    path('agregar-tip/', views.agregar_tip, name='agregar_tip'),
    path('about/', views.about, name='about'),
    path('pages/', listar_paginas, name='listar_paginas'),
    path('pages/<int:page_id>/', detalle_pagina, name='detalle_pagina'),
    path('pages/agregar/', agregar_pagina, name='agregar_pagina'),
    path('pages/<int:page_id>/editar/', editar_pagina, name='editar_pagina'),
    path('pages/<int:page_id>/eliminar/', eliminar_pagina, name='eliminar_pagina'),
]
