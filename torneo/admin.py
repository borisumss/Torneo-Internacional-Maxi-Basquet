from ast import Or
from django.contrib import admin
from .models import Torneo, Categorias_Torneo, Organizador, Equipo, Entrenador, Jugador, Delegado

# Register your models here.
admin.site.register(Torneo)
admin.site.register(Categorias_Torneo)
admin.site.register(Organizador)
admin.site.register(Equipo)
admin.site.register(Entrenador)
admin.site.register(Jugador)
admin.site.register(Delegado)
