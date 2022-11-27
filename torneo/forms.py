from dataclasses import field
# from tkinter import E
from django.forms import ModelForm
from django import forms
from .models import Organizador, Torneo, Categorias_Torneo , Equipo


class Create_Organizador(ModelForm):
    class Meta:
        model = Organizador
        fields = '__all__'

class Create_Torneo(ModelForm):
    class Meta:
        model = Torneo
        fields = '__all__'
###

######
class Create_Categorias_Torneo(ModelForm):
    class Meta:
        model = Categorias_Torneo
        fields = '__all__'

class EquipoForm(forms.ModelForm):

    nombre_equipo = forms.CharField(max_length=250)
    pais_origen = forms.CharField(max_length=250)
    ciudad_origen = forms.CharField(max_length=250)
    escudo_equipo =  forms.ImageField()
    portada_equipo =  forms.ImageField()


    class Meta:
        model = Equipo
        fields =  ('nombre_equipo',
                  'pais_origen',
                  'ciudad_origen',
                  'escudo_equipo',
                  'portada_equipo',
                  )

class EquipoFormIns(forms.ModelForm):

    nombre_equipo = forms.CharField(max_length=250)
    pais_origen = forms.CharField(max_length=250)
    ciudad_origen = forms.CharField(max_length=250)
    escudo_equipo =  forms.ImageField()
    portada_equipo =  forms.ImageField()
    categoria_equipo = forms.CharField(max_length=250)

    class Meta:
        model = Equipo
        fields =  ('nombre_equipo',
                  'pais_origen',
                  'ciudad_origen',
                  'escudo_equipo',
                  'portada_equipo',
                  'categoria_equipo',
                  )

class TorneoForm(forms.ModelForm):

    nombre_torneo = forms.CharField(max_length=250)
    fecha_torneo_inicio = forms.DateField()
    fecha_torneo_fin = forms.DateField()

    class Meta:
        model = Equipo
        fields =  ('nombre_torneo',
                  'fecha_torneo_inicio',
                  'fecha_torneo_fin',
                  )

class TorneoPreInsForm(forms.ModelForm):

    fecha_inicioPre = forms.DateField()
    fecha_finPre = forms.DateField()
    monto_Preinscripcion = forms.DecimalField()
    qr_Preinscripcion =  forms.ImageField()

    class Meta:
        model = Equipo
        fields =  ('fecha_inicioPre',
                  'fecha_finPre',
                  'monto_Preinscripcion',
                  'qr_Preinscripcion',
                  )

class TorneoRezForm(forms.ModelForm):

    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    monto_inscripcion = forms.DecimalField()
    qr_inscripcion =  forms.ImageField()

    class Meta:
        model = Equipo
        fields =  ('fecha_inicio',
                  'fecha_fin',
                  'monto_inscripcion',
                  'qr_inscripcion',
                  )