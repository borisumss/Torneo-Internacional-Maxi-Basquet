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
    class Meta:
        model = Equipo
        fields = '__all__'