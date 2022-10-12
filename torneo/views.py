#import email
#from typing_extensions import Self
from pickle import FALSE, TRUE
from unicodedata import category, name
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Organizador, Torneo, Etapa_Inscripcion, Categorias_Torneo, Etapa_PreInscripcion, delegado_Inscripcion, delegado_PreInscripcion
from django.contrib import messages
#def email_check(user):
#   return user.email.endswith('@admin2.com')
# Create your views here.
def index(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if request.user.email.endswith('@delegacion.com'):
                return redirect('delegacion')
            elif request.user.email.endswith('@admin.com'):
                return redirect('administracion')
        else:
            return render(request, 'index.html')
    
    

def login(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if request.user.email.endswith('@delegacion.com'):
                return redirect('delegacion')
            elif request.user.email.endswith('@admin.com'):
                return redirect('administracion')
        else:
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
            messages.warning(request, "Algo salio mal, intente nuevamente")
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
                logo = request.FILES.get('logo')
                id_organizador = organizador.pk
                torneo = Torneo(nombre_torneo=nombre_torneo, fecha_torneo_inicio=fecha_torneo_inicio, fecha_torneo_fin=fecha_torneo_fin, pais_torneo=pais_torneo, invitacion_documento=invitacion_documento, logo=logo ,id_organizador=organizador)
                torneo.save()
                
                #tipo_inscripcion_pre = 'pre inscripcion'
                fecha_inicio_pre = request.POST.get('fecha_preinscripcion_inicio')
                fecha_fin_pre = request.POST.get('fecha_preinscripcion_fin')
                monto_inscripcion_pre = request.POST.get('monto_preinscripcion')
                id_torneo = torneo.pk
                pre_inscripcion = Etapa_PreInscripcion(fecha_inicioPre=fecha_inicio_pre, fecha_finPre=fecha_fin_pre, monto_Preinscripcion=monto_inscripcion_pre, id_torneo=torneo)
                pre_inscripcion.save()

                #tipo_inscripcion_ins = 'inscripcion'
                fecha_inicio_ins = request.POST.get('fecha_inscripcion_inicio')
                fecha_fin_ins = request.POST.get('fecha_inscripcion_fin')
                monto_inscripcion_ins = request.POST.get('monto_inscripcion')
                inscripcion = Etapa_Inscripcion(fecha_inicio=fecha_inicio_ins, fecha_fin=fecha_fin_ins, monto_inscripcion=monto_inscripcion_ins, id_torneo=torneo)
                inscripcion.save()

                largo = len(request.POST.getlist('nombreCategoria'))
                for i in range(largo):
                    categoria = Categorias_Torneo(nombre_categoria=request.POST.getlist('nombreCategoria')[i], edad_minima=request.POST.getlist('minCategoria')[i], edad_maxima=request.POST.getlist('maxCategoria')[i], id_torneo=torneo)
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
                torneosProgreso = Torneo.objects.filter(torneo_estado=1)
                torneosTerminados = Torneo.objects.filter(torneo_estado=0)
                solicitudPre = delegado_PreInscripcion.objects.filter(estado_delegado_Preinscripcion='PENDIENTE')
                solicitudRez = delegado_Inscripcion.objects.filter(estado_delegado_inscripcion='PENDIENTE')
                return render(request, 'panelAdmin.html',{
                    "torneos":torneosProgreso, 
                    "torneosTerminados":torneosTerminados,
                    "solPre":solicitudPre,
                    "solRez":solicitudRez
                    })
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


def cerrarSesion(request):
    logout(request)
    return redirect('login')


def enviarSolicitud(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                return render(request, '')#La vista correspondiente
        else:
            return redirect('login')
    elif request.method == 'POST':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                #recibir por el POST si es "rezagados" o "preinscripcion"
                estado = request.POST.get('rezagados o preinscripcion')
                if estado == 'rezagados':
                    nombre_delegado_inscripcion = request.POST.get('atributo name del input del html')
                    estado_delegado_inscripcion = "PENDIENTE"
                    correo_delegado_inscripcion = request.POST.get('atributo name del input del html')
                    ci_delegado_inscripcion = request.POST.get('atributo name del input del html')
                    telefono_delegado_inscripcion = request.POST.get('atributo name del input del html')
                    id_etapa_inscripcion = request.POST.get('atributo name del input del html')
                    recibo_inscripcion = request.Files.get('atributo name del input del html')

                    solicitud = delegado_Inscripcion(nombre_delegado_inscripcion=nombre_delegado_inscripcion, estado_delegado_inscripcion=estado_delegado_inscripcion, correo_delegado_inscripcion=correo_delegado_inscripcion, ci_delegado_inscripcion=ci_delegado_inscripcion, telefono_delegado_inscripcion=telefono_delegado_inscripcion, id_etapa_inscripcion=id_etapa_inscripcion ,recibo_inscripcion=recibo_inscripcion)
                    solicitud.save()
                

                    return redirect('Vista correspondiente')
                else:
                    nombre_delegado_Preinscripcion = request.POST.get('atributo name del input del html')
                    estado_delegado_Preinscripcion = "PENDIENTE"
                    correo_delegado_Preinscripcion = request.POST.get('atributo name del input del html')
                    ci_delegado_Preinscripcion = request.POST.get('atributo name del input del html')
                    telefono_delegado_Preinscripcion = request.POST.get('atributo name del input del html')
                    id_etapa_Preinscripcion = request.POST.get('atributo name del input del html')
                    recibo_Preinscripcion = request.Files.get('atributo name del input del html')

                    solicitud = delegado_PreInscripcion(nombre_delegado_Preinscripcion=nombre_delegado_Preinscripcion, estado_delegado_Preinscripcion=estado_delegado_Preinscripcion, correo_delegado_Preinscripcion=correo_delegado_Preinscripcion, ci_delegado_Preinscripcion=ci_delegado_Preinscripcion, telefono_delegado_Preinscripcion=telefono_delegado_Preinscripcion, id_etapa_Preinscripcion=id_etapa_Preinscripcion ,recibo_Preinscripcion=recibo_Preinscripcion)
                    solicitud.save()
                

                    return redirect('Vista correspondiente')
               
        else:
            return redirect('login')