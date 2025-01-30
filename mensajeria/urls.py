from django.urls import path
from .views import enviar_mensaje, ver_mensajes

urlpatterns = [
    path('enviar/', enviar_mensaje, name='enviar_mensaje'),
    path('ver/', ver_mensajes, name='ver_mensajes'),
]
