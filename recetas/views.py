from django.shortcuts import render, get_object_or_404
from .models import Receta, Categoria, Bebida, Tip
from .forms import RecetaForm, ComentarioForm
from django.db.models import Q

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

def agregar_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'recetas/receta_creada.html')
    else:
        form = RecetaForm()
    return render(request, 'recetas/agregar_receta.html', {'form': form})

def listar_por_categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    recetas = Receta.objects.filter(categoria=categoria)
    return render(request, 'recetas/listar_por_categoria.html', {
        'categoria': categoria,
        'recetas': recetas
    })

def listar_bebidas(request):
    bebidas = Bebida.objects.all()
    return render(request, 'recetas/listar_bebidas.html', {'bebidas': bebidas})

def listar_tips(request):
    tips = Tip.objects.all()
    return render(request, 'recetas/listar_tips.html', {'tips': tips})

