from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    preparacion = models.TextField()
    imagen = models.ImageField(upload_to='recetas/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.receta.titulo}"


class Bebida(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(
        max_length=50,
        choices=[
            ('con_alcohol', 'Con Alcohol'),
            ('sin_alcohol', 'Sin Alcohol'),
        ]
    )
    preparacion = models.TextField()
    imagen = models.ImageField(upload_to='bebidas/', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Tip(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    categoria = models.CharField(
        max_length=50,
        choices=[
            ('tecnicas', 'Técnicas de Cocina'),
            ('herramientas', 'Herramientas Esenciales'),
            ('conservacion', 'Conservación de Alimentos'),
        ]
    )
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
