from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('ver_mensajes')
    else:
        form = MensajeForm()
    return render(request, "mensajeria/enviar_mensaje.html", {"form": form})

@login_required
def ver_mensajes(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user).order_by("-fecha_envio")
    mensajes_enviados = Mensaje.objects.filter(remitente=request.user).order_by("-fecha_envio")
    return render(request, "mensajeria/ver_mensajes.html", {"mensajes_recibidos": mensajes_recibidos, "mensajes_enviados": mensajes_enviados})
