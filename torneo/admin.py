from django.contrib import admin
from .models import *
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
    list_display = [f.name for f in Torneo._meta.fields]


@admin.register(Organizador)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Organizador._meta.fields]


@admin.register(Inscripcion)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Inscripcion._meta.fields]


@admin.register(Pre_Inscripcion)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Pre_Inscripcion._meta.fields]


@admin.register(delegado_Inscripcion)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in delegado_Inscripcion._meta.fields]


@admin.register(delegado_PreInscripcion)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in delegado_PreInscripcion._meta.fields]


@admin.register(Categorias_Torneo)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Categorias_Torneo._meta.fields]


@admin.register(Entrenador)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Entrenador._meta.fields]


@admin.register(Equipo)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Equipo._meta.fields]


@admin.register(Jugador)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Jugador._meta.fields]


@admin.register(Tabla_posiciones)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Tabla_posiciones._meta.fields]


@admin.register(Enfrentamiento)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Enfrentamiento._meta.fields]


@admin.register(Estadisticas_enfrentamiento)
class Torneo(admin.ModelAdmin):
    list_display = [f.name for f in Estadisticas_enfrentamiento._meta.fields]
