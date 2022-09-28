from dataclasses import field
from django.forms import ModelForm
from .models import Organizador, Torneo, Etapa_Inscripcion, Categorias_Torneo


class Create_Organizador(ModelForm):
    class Meta:
        model = Organizador
        fields = '__all__'

class Create_Torneo(ModelForm):
    class Meta:
        model = Torneo
        fields = '__all__'
###
class Create_Etapa_Inscripcion(ModelForm):
    class Meta:
        model = Etapa_Inscripcion
        fields = '__all__'
######
class Create_Categorias_Torneo(ModelForm):
    class Meta:
        model = Categorias_Torneo
        fields = '__all__'