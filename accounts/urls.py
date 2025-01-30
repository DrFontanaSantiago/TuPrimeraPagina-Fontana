from django.urls import path
from .views import registro, login_view, logout_view, perfil, editar_perfil
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
]
