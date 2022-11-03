from dataclasses import field
from tkinter import E
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