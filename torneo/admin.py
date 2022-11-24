from ast import Or
from django.contrib import admin
from .models import  Estadisticas_enfrentamiento,Enfrentamiento, Tabla_posiciones ,Torneo, Inscripcion, Pre_Inscripcion,Categorias_Torneo, Organizador, Equipo, Entrenador, Jugador, Delegado, delegado_Inscripcion, delegado_PreInscripcion 
# Register your models here.
# admin.site.register(Torneo)
# admin.site.register(Categorias_Torneo)
# admin.site.register(Organizador)
# admin.site.register(Equipo)
# admin.site.register(Entrenador)
# admin.site.register(Jugador)
# admin.site.register(Delegado)
# admin.site.register(Inscripcion)
# admin.site.register(Pre_Inscripcion)
# admin.site.register(delegado_Inscripcion)
# admin.site.register(delegado_PreInscripcion)
# admin.site.register(Estadisticas_enfrentamiento)
# admin.site.register(Enfrentamiento)

@admin.register(Torneo)
class Torneo(admin.ModelAdmin):
    list_display = ("nombre_torneo", "fecha_torneo_inicio", "fecha_torneo_fin")
    
@admin.register(Organizador)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(Inscripcion)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(Pre_Inscripcion)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(delegado_Inscripcion)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(delegado_PreInscripcion)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(Categorias_Torneo)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(Entrenador)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(Equipo)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(Jugador)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(Tabla_posiciones)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(Enfrentamiento)
class Torneo(admin.ModelAdmin):
    pass
@admin.register(Estadisticas_enfrentamiento)
class Torneo(admin.ModelAdmin):
    pass