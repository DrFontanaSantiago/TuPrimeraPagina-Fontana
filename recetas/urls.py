from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recetas/', views.listar_recetas, name='listar_recetas'),  
    path('recetas/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),  
    path('recetas/agregar/', views.agregar_receta, name='agregar_receta'), 
    path('categorias/<slug:slug>/', views.listar_por_categoria, name='listar_por_categoria'),
    path('bebidas/', views.listar_bebidas, name='listar_bebidas'),
    path('tips/', views.listar_tips, name='listar_tips'),
]
