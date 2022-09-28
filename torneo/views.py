#import email
#from typing_extensions import Self
from unicodedata import category, name
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Organizador, Torneo, Etapa_Inscripcion, Categorias_Torneo
#def email_check(user):
#   return user.email.endswith('@admin2.com')
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            if request.user.email.endswith('@delegacion.com'):
                return redirect('delegacion')
            elif request.user.email.endswith('@admin.com'):
                return redirect('administracion')
        else:
            return render(request, 'login.html')


    
#@login_required(redirect_field_name='home')

def crear_torneo(request):
    #print(request.user.is_authenticated)
    #print(request.user.is_anonymous)
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                return render(request, 'crearTorneo.html')
        else:
            return redirect('login')
    elif request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                #Organizador.nombre_organizador = request.POST.get('nombre_organizador')
                #Organizador.correo_organizador = request.POST.get('correo_organizador')
                #Organizador.telefono_organizador = request.POST.get('telefono_organizador')
                nombre_organizador = request.POST.get('nombre_organizador')
                correo_organizador = request.POST.get('correo_organizador')
                telefono_organizador = request.POST.get('telefono_organizador')
                organizador = Organizador(nombre_organizador=nombre_organizador, correo_organizador=correo_organizador, telefono_organizador=telefono_organizador)
                organizador.save()

                #Torneo.nombre_torneo = request.POST.get('nombre_torneo')
                #Torneo.fecha_torneo_inicio = request.POST.get('fecha_torneo_inicio')
                #Torneo.fecha_torneo_fin = request.POST.get('fecha_torneo_fin')
                #Torneo.pais_torneo = request.POST.get('pais_torneo')
                ##Torneo.torneo_estado = request.POST.get('')
                #Torneo.invitacion_documento = request.FILES.get('invitacion_documento')
                #Torneo.id_organizador = organizador.pk
                nombre_torneo = request.POST.get('nombre_torneo')
                fecha_torneo_inicio = request.POST.get('fecha_torneo_inicio')
                fecha_torneo_fin = request.POST.get('fecha_torneo_fin')
                pais_torneo = request.POST.get('pais_torneo')
                invitacion_documento = request.FILES.get('invitacion_documento')
                id_organizador = organizador.pk
                torneo = Torneo(nombre_torneo=nombre_torneo, fecha_torneo_inicio=fecha_torneo_inicio, fecha_torneo_fin=fecha_torneo_fin, pais_torneo=pais_torneo, invitacion_documento=invitacion_documento, id_organizador=organizador)
                torneo.save()
                
                tipo_inscripcion_pre = 'pre inscripcion'
                fecha_inicio_pre = request.POST.get('fecha_preinscripcion_inicio')
                fecha_fin_pre = request.POST.get('fecha_preinscripcion_fin')
                monto_inscripcion_pre = request.POST.get('monto_preinscripcion')
                id_torneo = torneo.pk
                pre_inscripcion = Etapa_Inscripcion(tipo_inscripcion=tipo_inscripcion_pre, fecha_inicio=fecha_inicio_pre, fecha_fin=fecha_fin_pre, monto_inscripcion=monto_inscripcion_pre, id_torneo=torneo)
                pre_inscripcion.save()

                tipo_inscripcion_ins = 'inscripcion'
                fecha_inicio_ins = request.POST.get('fecha_inscripcion_inicio')
                fecha_fin_ins = request.POST.get('fecha_inscripcion_fin')
                monto_inscripcion_ins = request.POST.get('monto_inscripcion')
                inscripcion = Etapa_Inscripcion(tipo_inscripcion=tipo_inscripcion_ins, fecha_inicio=fecha_inicio_ins, fecha_fin=fecha_fin_ins, monto_inscripcion=monto_inscripcion_ins, id_torneo=torneo)
                inscripcion.save()

                nombre_categoria = request.POST.get('nombre_categoria')
                edad_minima = request.POST.get('edad_minima')
                edad_maxima = request.POST.get('edad_maxima')
                categoria = Categorias_Torneo(nombre_categoria=nombre_categoria, edad_minima=edad_minima, edad_maxima=edad_maxima, id_torneo=torneo)
                categoria.save()

                return redirect('administracion')
        else:
            return redirect('login')
        
    
def administracion(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                torneos = Torneo.objects.all()
                return render(request, 'panelAdmin.html',{"torneos":torneos})
        else:
            return redirect('login')
    

def delegacion(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@delegacion.com'):
                return redirect('login')
            else:
                return render(request, 'panelDelegado.html')
        else:
            return redirect('login')
    