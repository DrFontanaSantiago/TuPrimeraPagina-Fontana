from django.contrib import admin
from django.urls import path, include
from recetas.views import acerca_de  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recetas.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', acerca_de, name='acerca_de'),  
    path('mensajeria/', include('mensajeria.urls')),
]
