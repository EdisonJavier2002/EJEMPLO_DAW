from django.contrib import admin
# Aquí importamos los modelos a este archivo
from.models import Genero, Director, Pais, Pelicula

# Register your models here.
admin.site.register(Genero)
admin.site.register(Director)
admin.site.register(Pais)
admin.site.register(Pelicula)

