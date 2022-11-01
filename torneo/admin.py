from ast import Or
from django.contrib import admin
from .models import Torneo, Inscripcion, Pre_Inscripcion,Categorias_Torneo, Organizador, Equipo, Entrenador, Jugador, Delegado, delegado_Inscripcion, delegado_PreInscripcion 
# Register your models here.
admin.site.register(Torneo)
admin.site.register(Categorias_Torneo)
admin.site.register(Organizador)
admin.site.register(Equipo)
admin.site.register(Entrenador)
admin.site.register(Jugador)
admin.site.register(Delegado)
admin.site.register(Inscripcion)
admin.site.register(Pre_Inscripcion)
admin.site.register(delegado_Inscripcion)
admin.site.register(delegado_PreInscripcion)