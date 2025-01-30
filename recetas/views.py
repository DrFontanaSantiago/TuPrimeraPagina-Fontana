from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Receta, Categoria, Bebida, Tip, Page
from .forms import RecetaForm, ComentarioForm, BebidaForm, TipForm, PageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Página de Inicio
def inicio(request):
    resultados_recetas = []
    resultados_bebidas = []
    resultados_tips = []

    if request.method == 'GET' and 'buscar' in request.GET:
        query = request.GET['buscar']
        resultados_recetas = Receta.objects.filter(
            Q(titulo__icontains=query) | Q(descripcion__icontains=query)
        )
        resultados_bebidas = Bebida.objects.filter(
            Q(titulo__icontains=query) | Q(descripcion__icontains=query)
        )
        resultados_tips = Tip.objects.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        )

    return render(
        request, 
        'inicio.html', 
        {
            'resultados_recetas': resultados_recetas,
            'resultados_bebidas': resultados_bebidas,
            'resultados_tips': resultados_tips,
        }
    )

# Recetas
def listar_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/listar_recetas.html', {'recetas': recetas})

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    comentarios = receta.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.receta = receta
            comentario.save()
            form = ComentarioForm()  
    else:
        form = ComentarioForm()

    return render(request, 'recetas/detalle_receta.html', {
        'receta': receta,
        'comentarios': comentarios,
        'form': form
    })

def listar_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    recetas = Receta.objects.filter(categoria=categoria)
    return render(request, 'recetas/listar_por_categoria.html', {
        'categoria': categoria,
        'recetas': recetas
    })

@login_required
def agregar_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Receta agregada correctamente.")
            return redirect('listar_recetas')
    else:
        form = RecetaForm()
    return render(request, 'recetas/agregar_receta.html', {'form': form})

# Bebidas
def listar_bebidas(request):
    bebidas = Bebida.objects.all()
    return render(request, 'bebidas/listar_bebidas.html', {'bebidas': bebidas})

@login_required
def agregar_bebida(request):
    if request.method == 'POST':
        form = BebidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Bebida agregada correctamente.")
            return redirect('listar_bebidas')
    else:
        form = BebidaForm()
    return render(request, 'bebidas/agregar_bebida.html', {'form': form})

def detalle_bebida(request, bebida_id):
    bebida = get_object_or_404(Bebida, id=bebida_id)
    return render(request, 'bebidas/detalle_bebida.html', {'bebida': bebida})

# Tips
def listar_tips(request):
    tips = Tip.objects.all()
    return render(request, 'tips/listar_tips.html', {'tips': tips})

def detalle_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    return render(request, 'tips/detalle_tip.html', {'tip': tip})

@login_required
def agregar_tip(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tip agregado correctamente.")
            return redirect('listar_tips')
    else:
        form = TipForm()
    return render(request, 'tips/agregar_tip.html', {'form': form})

# Acerca de mí
def about(request):
    return render(request, 'about.html')

def acerca_de(request):
    return render(request, 'about.html')

# Páginas 
def listar_paginas(request):
    paginas = Page.objects.all().order_by('-fecha_creacion')
    return render(request, 'pages/listar_paginas.html', {'paginas': paginas})

def detalle_pagina(request, page_id):
    pagina = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/detalle_pagina.html', {'pagina': pagina})

@login_required
def agregar_pagina(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_pagina = form.save(commit=False)
            nueva_pagina.autor = request.user
            nueva_pagina.save()
            messages.success(request, "Publicación agregada correctamente.")
            return redirect('listar_paginas')
    else:
        form = PageForm()
    return render(request, 'pages/agregar_pagina.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

@login_required
def editar_pagina(request, page_id):
    pagina = get_object_or_404(Page, id=page_id)
    
    if request.user != pagina.autor:
        messages.error(request, "No tienes permiso para editar esta publicación.")
        return redirect('listar_paginas')

    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=pagina)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación actualizada con éxito.")
            return redirect('detalle_pagina', page_id=pagina.id)
    else:
        form = PageForm(instance=pagina)

    return render(request, 'pages/editar_pagina.html', {'form': form, 'pagina': pagina})

@login_required
def eliminar_pagina(request, page_id):
    pagina = get_object_or_404(Page, id=page_id)

    if request.user != pagina.autor:
        messages.error(request, "No tienes permiso para eliminar esta publicación.")
        return redirect('listar_paginas')

    pagina.delete()
    messages.success(request, "Publicación eliminada con éxito.")
    return redirect('listar_paginas')
