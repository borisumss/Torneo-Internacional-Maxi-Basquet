#import email
#from typing_extensions import Self
import email
from pickle import FALSE, TRUE
from re import I
from sqlite3 import PrepareProtocol
from unicodedata import category, name
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Organizador, Torneo, Enfrentamiento,Tabla_posiciones,Inscripcion, Categorias_Torneo, Pre_Inscripcion, delegado_Inscripcion, delegado_PreInscripcion , Entrenador, Equipo ,Delegado , Jugador
from django.contrib import messages
from datetime import date
from django.core.mail import send_mail
from django.conf import settings
import random as rd
from qr_code.qrcode.utils import MeCard
from .forms import EquipoForm, TorneoForm, TorneoPreInsForm, TorneoRezForm
# def email_check(user):
#   return user.email.endswith('@admin2.com')
# Create your views here.

"""
# CODIGO PARA GUARDAR USUARIO
user = User.objects.create_user(username= ,password= ,email=)
user.save()
# CODIGO PARA MANDAR EMAIL
subject = 'Bienvenido al Torneo de Maxi Basquet'
message = f'Hola delegado estas son sus credenciales para acceder y registrr su equipo en el torneo nombre de usuario: {username} contraseña: {password}'
from_email = settings.EMAIL_HOST_USER
recipient_list = [email]
send_mail(subject, message, from_email, recipient_list, fail_silently=False)
"""


def index(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if request.user.email.endswith('@delegacion.com'):
                return redirect('delegacionTorneo')
            elif request.user.email.endswith('@admin.com'):
                return redirect('torneos')
        else:
            torneosProgreso = Torneo.objects.filter(torneo_estado=1)
            aux = []
            for i in range(len(torneosProgreso)):
                aux.append(i+1)
            return render(request, 'index.html', {
                "torneos": torneosProgreso,
                "longitud": aux
            })


def preinscripcion(request, id):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if request.user.email.endswith('@delegacion.com'):
                return redirect('delegacionTorneo')
            elif request.user.email.endswith('@admin.com'):
                return redirect('torneos')
        else:
            Preins = Pre_Inscripcion.objects.filter(id_torneo_id=id)
            Ins = Inscripcion.objects.filter(id_torneo_id=id)
            now = date.today()
            # if (len(Preins) == 1 and len(Ins) == 1):
            if (1==1):
                if (now >= Preins[0].fecha_inicioPre and now <= Preins[0].fecha_finPre):
                    return render(request, 'pagoPreinscripcion.html',
                                  {'etapa': "PRE-INSCRIPCION",
                                   'monto': Preins[0].monto_Preinscripcion,
                                   'torneo': Preins[0].id_torneo.nombre_torneo,
                                   'qr': Preins[0].qr_Preinscripcion
                                   })
                elif (now >= Ins[0].fecha_inicio and now <= Ins[0].fecha_fin):
                    return render(request, 'pagoPreinscripcion.html',
                                  {'etapa': "REZAGADOS",
                                   'monto': Ins[0].monto_inscripcion,
                                      'torneo': Ins[0].id_torneo.nombre_torneo,
                                      'qr': Ins[0].qr_inscripcion
                                   })
                else:
                    if (now < Ins[0].fecha_inicio) or (now < Preins[0].fecha_inicioPre):
                        messages.warning(
                            request, "Aún faltan días para la Pre-Inscripción")
                    else:
                        messages.warning(
                            request, "Lo sentimos, termino el plazo para la pre-inscripcion")
                    return redirect('home')
            else:
                messages.warning(request, "Algo salio mal, intente nuevamente")
                return redirect('home')
    elif request.method == 'POST':
        return enviarSolicitud(request, id)


def login(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if request.user.email.endswith('@delegacion.com'):
                return redirect('delegacionTorneo')
            elif request.user.email.endswith('@admin.com'):
                return redirect('torneos')
        else:
            return render(request, 'login.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            rez = delegado_Inscripcion.objects.filter(id_delegadoIns_id=user.pk)
            pre = delegado_PreInscripcion.objects.filter(id_delegadoPreIns_id=user.pk)
            if len(rez)>0:
                if rez[0].estado_delegado_inscripcion == 'BAJA':
                    messages.warning(request, "Este usuario ha sido dado de baja")
                    return render(request, 'login.html')
                else:
                    auth_login(request, user)
                    return redirect('delegacionTorneo')
            
            elif len(pre)>0:
                if pre[0].estado_delegado_Preinscripcion=='BAJA':
                    messages.warning(request, "Este usuario ha sido dado de baja")
                    return render(request, 'login.html')
                else:
                    auth_login(request, user)
                    return redirect('delegacionTorneo')
                    
            else:
                auth_login(request, user)
                return redirect('torneos')
        else:
            messages.warning(request, "Algo salio mal, intente nuevamente")
            return render(request, 'login.html')


# @login_required(redirect_field_name='home')

def crear_torneo(request):
    # print(request.user.is_authenticated)
    # print(request.user.is_anonymous)
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
                organizador = Organizador(nombre_organizador=nombre_organizador,
                                          correo_organizador=correo_organizador, telefono_organizador=telefono_organizador)
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
                invitacion_documento = request.FILES.get(
                    'invitacion_documento')
                logo = request.FILES.get('logo')
                id_organizador = organizador.pk
                torneo = Torneo(nombre_torneo=nombre_torneo, fecha_torneo_inicio=fecha_torneo_inicio, fecha_torneo_fin=fecha_torneo_fin,
                                pais_torneo=pais_torneo, invitacion_documento=invitacion_documento, logo=logo, id_organizador=organizador)
                torneo.save()

                #tipo_inscripcion_pre = 'pre inscripcion'
                fecha_inicio_pre = request.POST.get(
                    'fecha_preinscripcion_inicio')
                fecha_fin_pre = request.POST.get('fecha_preinscripcion_fin')
                monto_inscripcion_pre = request.POST.get(
                    'monto_preinscripcion')
                qr1 = request.FILES.get('qr1_torneo')
                id_torneo = torneo.pk
                pre_inscripcion = Pre_Inscripcion(
                    qr_Preinscripcion=qr1,fecha_inicioPre=fecha_inicio_pre, fecha_finPre=fecha_fin_pre, monto_Preinscripcion=monto_inscripcion_pre, id_torneo=torneo)
                pre_inscripcion.save()

                #tipo_inscripcion_ins = 'inscripcion'
                fecha_inicio_ins = request.POST.get('fecha_inscripcion_inicio')
                fecha_fin_ins = request.POST.get('fecha_inscripcion_fin')
                monto_inscripcion_ins = request.POST.get('monto_inscripcion')
                qr2 = request.FILES.get('qr2_torneo')
                inscripcion = Inscripcion(qr_inscripcion=qr2,fecha_inicio=fecha_inicio_ins, fecha_fin=fecha_fin_ins,
                                          monto_inscripcion=monto_inscripcion_ins, id_torneo=torneo)
                inscripcion.save()

                largo = len(request.POST.getlist('nombreCategoria'))
                for i in range(largo):
                    categoria = Categorias_Torneo(nombre_categoria=request.POST.getlist('nombreCategoria')[i], edad_minima=request.POST.getlist(
                        'minCategoria')[i], edad_maxima=request.POST.getlist('maxCategoria')[i], id_torneo=torneo)
                    categoria.save()

                return redirect('torneos')
        else:
            return redirect('login')


def administracion(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                return redirect('torneos')
        else:
            return redirect('login')


def delegacion(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@delegacion.com'):
                return redirect('login')
            else:
                return redirect('delegacionTorneo')
        else:
            return redirect('login')


def cerrarSesion(request):
    logout(request)
    return redirect('login')


def enviarSolicitud(request, id):
    # recibir por el POST si es "rezagados" o "preinscripcion"
    estado = request.POST.get('Confirmar')
    inscritoPre = delegado_PreInscripcion.objects.filter(ci_delegado_Preinscripcion=request.POST.get('ci_delegado'))
    inscritoRez = delegado_Inscripcion.objects.filter(ci_delegado_inscripcion=request.POST.get('ci_delegado'))
    #A FUTURO:
    #si el usuario ya existe y tiene estado "RECHAZADO" o "BAJA" se actualizan sus datos y su estado cambia a "PENDIENTE"
    #si el usuario ya existe y tiene estado "PENDIENTE" o "ACEPTADO" se rechaza la solicitud
    if len(inscritoPre)>0 or len(inscritoRez)>0:
        messages.error(request, "Ya se encuentra un usuario registrado con estos datos")
        return redirect('home')

    elif estado == 'REZAGADOS':
        print(request.FILES)
        aux = Inscripcion.objects.filter(id_torneo_id=id)
        nombre_delegado_inscripcion = request.POST.get('nombre_delegado')
        estado_delegado_inscripcion = "PENDIENTE"
        correo_delegado_inscripcion = request.POST.get('correo_delegado')
        ci_delegado_inscripcion = request.POST.get('ci_delegado')
        telefono_delegado_inscripcion = request.POST.get('telef_delegado')
        id_etapa_inscripcion = aux[0]
        recibo_inscripcion = request.FILES.get('img_comprobante')
        print(recibo_inscripcion)
        solicitud = delegado_Inscripcion(nombre_delegado_inscripcion=nombre_delegado_inscripcion, estado_delegado_inscripcion=estado_delegado_inscripcion, correo_delegado_inscripcion=correo_delegado_inscripcion,
                                         ci_delegado_inscripcion=ci_delegado_inscripcion, telefono_delegado_inscripcion=telefono_delegado_inscripcion, id_inscripcion=id_etapa_inscripcion, recibo_inscripcion=recibo_inscripcion)
        solicitud.save()

        messages.success(request, "Solicitud Enviada correctamente")
        return redirect('home')
    elif estado == 'PRE-INSCRIPCION':
        aux = Pre_Inscripcion.objects.filter(id_torneo_id=id)
        nombre_delegado_Preinscripcion = request.POST.get('nombre_delegado')
        estado_delegado_Preinscripcion = "PENDIENTE"
        correo_delegado_Preinscripcion = request.POST.get('correo_delegado')
        ci_delegado_Preinscripcion = request.POST.get('ci_delegado')
        telefono_delegado_Preinscripcion = request.POST.get('telef_delegado')
        id_etapa_Preinscripcion = aux[0]
        recibo_Preinscripcion = request.FILES.get('img_comprobante')

        # print(recibo_Preinscripcion)
        solicitud = delegado_PreInscripcion(nombre_delegado_Preinscripcion=nombre_delegado_Preinscripcion, estado_delegado_Preinscripcion=estado_delegado_Preinscripcion, correo_delegado_Preinscripcion=correo_delegado_Preinscripcion,
                                            ci_delegado_Preinscripcion=ci_delegado_Preinscripcion, telefono_delegado_Preinscripcion=telefono_delegado_Preinscripcion, id_Pre_inscripcion=id_etapa_Preinscripcion, recibo_Preinscripcion=recibo_Preinscripcion)

        solicitud.save()

        messages.success(request, "Solicitud Enviada correctamente")
        return redirect('home')


def rechazar(request, tipo, id):

    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                if tipo == 'REZAGADOS':
                    ins = delegado_Inscripcion.objects.filter(id=id)
                    aux = ins[0].estado_delegado_inscripcion
                    if len(ins)==0:
                        return redirect('solicitudes')
                    else:
                        if aux == 'PENDIENTE':
                            return render(request, 'emails.html',{
                            "email":ins[0].correo_delegado_inscripcion,
                            "tipo":"RECHAZO",
                            "id":ins[0].correo_delegado_inscripcion
                            })
                            """solicitud = delegado_Inscripcion.objects.filter(id=id)
                            solicitud.update(estado_delegado_inscripcion='RECHAZADO')
                            messages.success(request, "Solictud rechazada correctamente")"""
                        else:
                            messages.success(request, "La solicitud no se encuentra disponible")
                            return redirect('solicitudes')
                elif tipo == 'PREINSCRIPCION':
                    preIns = delegado_PreInscripcion.objects.filter(id=id)
                    aux = preIns[0].estado_delegado_Preinscripcion
                    if len(preIns)==0:
                        return redirect('solicitudes')
                    else:
                        if aux == 'PENDIENTE':

                            return render(request, 'emails.html',{
                            "email":preIns[0].correo_delegado_Preinscripcion,
                            "tipo":"RECHAZO",
                            "id":preIns[0].correo_delegado_Preinscripcion
                            })
                            """solicitud = delegado_PreInscripcion.objects.filter(id=id)
                            solicitud.update(estado_delegado_Preinscripcion='RECHAZADO')
                            messages.success(request, "Solictud rechazada correctamente")"""
                        else:
                           messages.success(request, "La solicitud no se encuentra disponible")
                           return redirect('solicitudes')
                else:
                    return redirect('solicitudes')

        else:
            return redirect('login')
    elif request.method == 'POST':
        if tipo == 'REZAGADOS':
            solicitud = delegado_Inscripcion.objects.filter(id=id)
            correo = request.POST.get('email')
            solicitud.update(estado_delegado_inscripcion='RECHAZADO')
            subject = 'Solicitud Rechazada para el Torneo de Maxi Basquet'
            message = f'Tenga coordiales saludos.\n\nA continuación se presenta el motivo de su rechazo:\n' + \
                request.POST.get('motivo') + '\n\nAtte: ' + \
                request.user.username + ", "+request.user.email
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [correo]
            send_mail(subject, message, from_email,
                      recipient_list, fail_silently=False)
            messages.success(request, "Solictud rechazada correctamente")

        elif tipo == 'PREINSCRIPCION':
            solicitud = delegado_PreInscripcion.objects.filter(id=id)
            correo = request.POST.get('email')
            solicitud.update(estado_delegado_Preinscripcion='RECHAZADO')

            subject = 'Solicitud Rechazada para el Torneo de Maxi Basquet'
            message = f'Tenga coordiales saludos. A continuación se presenta el motivo de su rechazo:\n' + \
                request.POST.get('motivo')
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [correo]
            send_mail(subject, message, from_email,
                      recipient_list, fail_silently=False)
            messages.success(request, "Solictud rechazada correctamente")
        return redirect('solicitudes')

 
def aceptar(request, tipo, id):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                if tipo == 'REZAGADOS':
                    ins = delegado_Inscripcion.objects.filter(id=id)
                    aux = ins[0].estado_delegado_inscripcion
                    if len(ins)==0:
                        return redirect('solicitudes')
                    else:
                        if aux == 'PENDIENTE':
                            return render(request, 'emails.html',{
                            "email":ins[0].correo_delegado_inscripcion,
                            "tipo":"ACEPTADO",
                            "id":id
                            })
                            """solicitud = delegado_Inscripcion.objects.filter(id=id)
                            solicitud.update(estado_delegado_inscripcion='RECHAZADO')
                            messages.success(request, "Solictud rechazada correctamente")"""
                        else:
                            messages.success(request, "La solicitud no se encuentra disponible")
                            return redirect('solicitudes')

                elif tipo == 'PREINSCRIPCION':
                    preIns = delegado_PreInscripcion.objects.filter(id=id)
                    aux = preIns[0].estado_delegado_Preinscripcion
                    if len(preIns)==0:
                        return redirect('solicitudes')
                    else:
                        if aux == 'PENDIENTE':
                            return render(request, 'emails.html',{
                            "email":preIns[0].correo_delegado_Preinscripcion,
                            "tipo":"ACEPTADO",
                            "id":id
                            })
                            """solicitud = delegado_PreInscripcion.objects.filter(id=id)
                            solicitud.update(estado_delegado_Preinscripcion='RECHAZADO')
                            messages.success(request, "Solictud rechazada correctamente")"""
                        else:
                            messages.success(request, "La solicitud no se encuentra disponible")
                            return redirect('solicitudes')
                else:
                    return redirect('solicitudes')

        else:
            return redirect('login')
    elif request.method == 'POST':
        letras = "abcdefghijklmnopqestuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros = "0123456789"
        unido = f'{letras}{numeros}'
        contrasenia = ''.join(rd.sample(unido, 10))
        correo = request.POST.get('correo')
        usuario = request.POST.get('username')
        user = User.objects.create_user(
            username=usuario, password=contrasenia, email=correo)
        user.save()
        if tipo == 'REZAGADOS':
            solicitud = delegado_Inscripcion.objects.filter(id=id)
            solicitud.update(estado_delegado_inscripcion='ACEPTADO',id_delegadoIns_id=user.pk)
            id_delegado = user.pk
            nombre_delegado = solicitud[0].nombre_delegado_inscripcion
            ci_delegado = solicitud[0].ci_delegado_inscripcion
            telefono_delegado  = solicitud[0].telefono_delegado_inscripcion
            delegado = Delegado(id_delegado=id_delegado, nombre_delegado=nombre_delegado,ci_delegado= ci_delegado,telefono_delegado=telefono_delegado)
            delegado.save()

            #datos equipo
            estado_inscrip = 'PENDIENTE'
            id_deleg = delegado
            id_torneo = solicitud[0].id_inscripcion.id_torneo
            portada = 'static/imagenes/equipos/portadas/default.jpg' 
            escudo = 'static/imagenes/equipos/escudos/default.jpg'
            equipo = Equipo(estado_inscripcion_equipo=estado_inscrip,id_delegado=id_deleg,id_torneo=id_torneo, escudo_equipo = escudo, portada_equipo = portada)
            equipo.save()
                  
        elif tipo == 'PREINSCRIPCION':            
            solicitud = delegado_PreInscripcion.objects.filter(id=id)
            solicitud.update(estado_delegado_Preinscripcion='ACEPTADO',id_delegadoPreIns_id=user.pk)
            id_delegado = user.pk
            nombre_delegado = solicitud[0].nombre_delegado_Preinscripcion
            ci_delegado = solicitud[0].ci_delegado_Preinscripcion
            telefono_delegado  = solicitud[0].telefono_delegado_Preinscripcion
            delegado = Delegado(id_delegado=id_delegado, nombre_delegado=nombre_delegado,ci_delegado= ci_delegado,telefono_delegado=telefono_delegado)
            delegado.save()

            #datos equipo
            estado_inscrip = 'PENDIENTE'
            id_deleg = delegado
            id_torneo = solicitud[0].id_Pre_inscripcion.id_torneo
            equipo = Equipo(estado_inscripcion_equipo=estado_inscrip,id_delegado=id_deleg,id_torneo=id_torneo)
            equipo.save()

        subject = 'Bienvenido al Torneo de Maxi Basquet'
        message = f'Tenga coordiales saludos.\n\nA continuación se presenta sus credenciales para acceder y registrar a su equipo en el torneo.\n\nNombre de usuario: ' + \
            usuario + '\nContraseña: '+contrasenia+'\nEmail: '+correo + \
            '\n\nAtte: ' + request.user.username + ", "+request.user.email
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get('email')]
        # send_mail(subject, message, from_email,
                #   recipient_list, fail_silently=False)
        # messages.success(request, "Solictud Aceptada correctamente")
        print(message)
        return redirect('solicitudes')


def verTorneo(request, id):
    tablas = Tabla_posiciones.objects.filter(id_torneo=id)   
    torneo = Torneo.objects.filter(id=id)
    if request.method == 'GET':
        categorias = Categorias_Torneo.objects.filter(id_torneo=id)
        equipos = Equipo.objects.filter(estado_inscripcion_equipo="INSCRITO", id_torneo=id)
        enfrentamientos = Enfrentamiento.objects.filter(id_torneo=id) 
        nueva = sorted(tablas, key=lambda x: x.puntaje_total, reverse=True) 
        nuevaVs = sorted(enfrentamientos, key=lambda x: x.fecha_enfrentamiento) 
        numeros = len(tablas)  
        return render(request, 'Torneo.html', {
            "torneo": torneo,
            "categorias": categorias,
            "equipos": equipos,
            "tablas": nueva,
            "numeros": numeros,
            "enfrentamientos": nuevaVs,
        })
    elif request.method == 'POST':
        for i in range(len(tablas)):
            for j in range(len(tablas)):
                if i != j:
                    if tablas[i].categoria_equipo == tablas[j].categoria_equipo:
                        equipo_a = tablas[i].nombre_equipo
                        escudoA = tablas[i].escudo_equipo
                        equipo_b = tablas[j].nombre_equipo
                        escudoB = tablas[j].escudo_equipo
                        categoria = tablas[i].categoria_equipo
                        estado = 'PENDIENTE'
                        enfrentamiento = Enfrentamiento(escudo_equipoA=escudoA,escudo_equipoB=escudoB,estado=estado,equipo_a=equipo_a,equipo_b=equipo_b, categoria = categoria, id_torneo = torneo[0])
                        enfrentamiento.save()
        
        return redirect('Torneo',id)

def administracionTorneos(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                torneosProgreso = Torneo.objects.filter(torneo_estado=1)
                return render(request, 'Tab1.html', {
                    "torneos": torneosProgreso,
                })
        else:
            return redirect('login')


def administracionTorneosTerminados(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                torneosTerminados = Torneo.objects.filter(torneo_estado=0)
                return render(request, 'Tab2.html', {
                    "torneosTerminados": torneosTerminados
                })
        else:
            return redirect('login')


def administracionSolicitudes(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                solicitudPre = delegado_PreInscripcion.objects.filter(
                    estado_delegado_Preinscripcion='PENDIENTE')
                solicitudRez = delegado_Inscripcion.objects.filter(
                    estado_delegado_inscripcion='PENDIENTE')
                return render(request, 'Tab5.html', {
                    "solPre": solicitudPre,
                    "solRez": solicitudRez
                })
        else:
            return redirect('login')
    elif request.method == 'POST':
        letras = "abcdefghijklmnopqestuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros = "0123456789"
        unido = f'{letras}{numeros}'
        contrasenia = ''.join(rd.sample(unido, 10))
        correo = request.POST.get('email')
        usuario = request.POST.get('username')
        user = User.objects.create_user(
            username=usuario, password=contrasenia, email=correo)
        user.save()
        subject = 'Bienvenido al Torneo de Maxi Basquet'
        message = f'Tenga coordiales saludos. A continuación se presenta sus credenciales para acceder y registrar a su equipo en el torneo.\nNombre de usuario: ' + \
            request.POST.get('username')+'\nContraseña: '+contrasenia
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get('email')]
        send_mail(subject, message, from_email,
                  recipient_list, fail_silently=False)

        messages.success(request, "Solicitud Aceptada correctamente")
        return redirect('solicitudes')


def administracionDelegados(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                delPre = delegado_PreInscripcion.objects.filter(estado_delegado_Preinscripcion='ACEPTADO')
                delRez = delegado_Inscripcion.objects.filter(estado_delegado_inscripcion='ACEPTADO')
                preBaja = delegado_PreInscripcion.objects.filter(estado_delegado_Preinscripcion='BAJA')
                rezBaja = delegado_Inscripcion.objects.filter(estado_delegado_inscripcion='BAJA')
                return render(request, 'Tab3.html',{
                    'pre':delPre,
                    'rez':delRez,
                    'preBaja':preBaja,
                    'rezBaja':rezBaja})
        else:
            return redirect('login')


def delegadosBaja(request,tipo,id):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                print(tipo)
                if(tipo == 'PREINSCRIPCION'):
                    delegado = delegado_PreInscripcion.objects.filter(id=id)
                    delegado.update(estado_delegado_Preinscripcion='BAJA')
                    messages.success(request, "Delegado dado de baja correctamente")
                    return redirect('delegados')
                elif tipo == 'REZAGADOS':
                    delegado = delegado_Inscripcion.objects.filter(id=id)
                    delegado.update(estado_delegado_inscripcion='BAJA')
                    messages.success(request, "Delegado dado de baja correctamente")
                    return redirect('delegados')
        else:
            return redirect('login')

def delegadosAlta(request,tipo,id):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                if(tipo == 'PREINSCRIPCION'):
                    delegado = delegado_PreInscripcion.objects.filter(id=id)
                    delegado.update(estado_delegado_Preinscripcion='ACEPTADO')
                    messages.success(request, "Delegado dado de alta correctamente")
                    return redirect('delegados')
                elif tipo == 'REZAGADOS':
                    delegado = delegado_Inscripcion.objects.filter(id=id)
                    delegado.update(estado_delegado_inscripcion='ACEPTADO')
                    messages.success(request, "Delegado dado de alta correctamente")
                    return redirect('delegados')
        else:
            return redirect('login')


def administracionEquipos(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                torneo_actual = get_object_or_404(Torneo, torneo_estado=1) #peligroso
                categorias = Categorias_Torneo.objects.filter(id_torneo=torneo_actual.pk)
                equipos = Equipo.objects.filter(estado_inscripcion_equipo="INSCRITO", id_torneo=torneo_actual.pk)
                return render(request, 'Tab4.html', {
                    'equipos': equipos,
                    'categorias': categorias,
                })
        else:
            return redirect('login')

def verEquipo(request, idequipo):
    if request.method == 'GET':        
        equipo = Equipo.objects.get(id=idequipo)
        cate = Categorias_Torneo.objects.filter(id_torneo=equipo.id_torneo)
        fechas = Inscripcion.objects.filter(id_torneo=equipo.id_torneo)
        jugadores = Jugador.objects.filter(id_equipo=equipo)
        return render(request, 'mostrar_detalle_equipo.html', {
                    'equipo': equipo,
                    'categorias': cate,
                    'jugadores': jugadores,
                    'fechas': fechas.first(),
                })

    # elif request.method == 'POST':
    #     numeros = "0123456789"
    #     unido = f'{letras}{numeros}'
    #     contrasenia = ''.join(rd.sample(unido, 10))
    #     correo = request.POST.get('email')
    #     usuario = request.POST.get('username')
    #     user = User.objects.create_user(
    #         username=usuario, password=contrasenia, email=correo)
    #     user.save()
    #     subject = 'Bienvenido al Torneo de Maxi Basquet'
    #     message = f'Tenga coordiales saludos. A continuación se presenta sus credenciales para acceder y registrar a su equipo en el torneo.\nNombre de usuario: ' + \
    #         request.POST.get('username')+'\nContraseña: '+contrasenia
    #     from_email = settings.EMAIL_HOST_USER
    #     recipient_list = [request.POST.get('email')]
    #     send_mail(subject, message, from_email,
    #               recipient_list, fail_silently=False)

    #     messages.success(request, "Solicitud Aceptada correctamente")
    #     return redirect('solicitudes')


def delegacionTorneo(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@delegacion.com'):
                return redirect('login')
            else:
                equipo = Equipo.objects.filter(id_delegado=request.user.id)
                return render(request,'Tab1Del.html',{
                    'equipo':equipo[0]
                })
               
        else:
            return redirect('login')

def delegacionEquipo(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@delegacion.com'):
                return redirect('login')
            else:
               equipo = Equipo.objects.filter(id_delegado=request.user.id)
               todos = Equipo.objects.all()
               aux = ''
               for i in todos:
                    if i != equipo[0]:
                        if i.nombre_equipo is not None:
                            aux = aux + i.nombre_equipo +"-"

               cate = Categorias_Torneo.objects.filter(id_torneo=equipo[0].id_torneo)
               fechas = Inscripcion.objects.filter(id_torneo=equipo[0].id_torneo)
               jugadores = Jugador.objects.filter(id_equipo = equipo[0])
               print(equipo[0])
               return render(request,'Tab2Del.html',{
                    'equipo':equipo[0],
                    'categorias':cate,
                    'jugadores': jugadores,
                    'fechas':fechas.first(),
                    'equiposTodos':aux
                })
        else:
            return redirect('login')
    elif request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        #portada ="static/imagenes/equipos/portadas/" + str(request.FILES.get('portada_equipo'))
        #escudo = "static/imagenes/equipos/escudos/"+ str( request.FILES.get('escudo_equipo'))
        portada =request.FILES.get('portada_equipo')
        escudo = request.FILES.get('escudo_equipo')

        nombre = request.POST.get('nombre_equipo')
        pais = request.POST.get('pais_equipo')
        ciudad = request.POST.get('ciudad_equipo')
        categoria = request.POST.get('categoria_equipo')
         
        """ equipo = Equipo.objects.filter(id_delegado=request.user.id)
        estado = 'INSCRITO'
       
        equipo.update(pais_origen = pais, ciudad_origen= ciudad, nombre_equipo = nombre, categoria_equipo=categoria, estado_inscripcion_equipo=estado)
        """
        equipo = Equipo.objects.get(id_delegado=request.user.id)
        print(equipo)
        form = EquipoForm(request.POST or None, request.FILES or None,instance = equipo)
        print("*************"*4)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, "Informació registrada correctamente")
            
        else:
            messages.error(request, "Algo salio mal, intente nuevamente")
        
        return redirect('delegacionEquipo')

def delegacionCredenciales(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@delegacion.com'):
                return redirect('login')
            else:
                equipo = Equipo.objects.filter(id_delegado=request.user.id)[0]
                jugadores = Jugador.objects.filter(id_equipo=equipo.pk)
                entrenador = Entrenador.objects.get(id=equipo.id_entrenador_equipo.pk)
                delegado = Delegado.objects.get(id_delegado=equipo.id_delegado.pk)

                return render(request,'Tab3Del.html',{
                    'jugadores': jugadores,
                    'entrenador': entrenador,
                    'delegado': delegado,
                })
        else:
            return redirect('login')


def view_card(request, pk=None):
    if pk is None:
        return HttpResponse("Jugador ID is Invalid")
    elif(Jugador.objects.filter(ci_jugador=pk).exists()):
        jugador = Jugador.objects.get(ci_jugador=pk)
        info_jugador = MeCard(
            name=jugador.nombre_jugador,
            phone=jugador.ci_jugador,
            email=jugador.apodo_jugador,
            url=jugador.dorsal_jugador,
            birthday='',
            memo=jugador.posicion_jugador,
            org=''
        )
        return render(request, 'view_id.html',{ 
        'jugador': jugador,
        'info_jugador': info_jugador,
        })
    elif(Entrenador.objects.filter(ci_entrenador=pk).exists()):
        entrenador = Entrenador.objects.get(ci_entrenador=pk)
        info_entrenador = MeCard(
            name=entrenador.nombre_entrenador,
            phone=entrenador.ci_entrenador,
            email=entrenador.apodo_entrenador,
            url=entrenador.nacionalidad_entrenador,
            birthday='',
            memo='',
            org=''
        )
        return render(request, 'view_id_entrenador.html', {
            'entrenador': entrenador,
            'info_entrenador': info_entrenador,
        })
    else:
        delegado = Delegado.objects.get(ci_delegado=pk)
        info_delegado = MeCard(
            name=delegado.nombre_delegado,
            phone=delegado.ci_delegado,
            email='',
            url='',
            birthday='',
            memo='',
            org=''
        )
        return render(request, 'view_id_delegado.html', {
            'delegado': delegado,
            'info_delegado': info_delegado,
        })


def view_card_entrenador(request, pk=None):
    if pk is None:
        return HttpResponse("Entrenador ID is Invalid")
    else:
        entrenador = Entrenador.objects.get(ci_entrenador=pk)
        info_entrenador = MeCard(
            name=entrenador.nombre_entrenador,
            phone=entrenador.ci_entrenador,
            email=entrenador.apodo_entrenador,
            url=entrenador.nacionalidad_entrenador,
            birthday='',
            memo='',
            org=''
        )
        return render(request, 'view_id_entrenador.html', {
            'entrenador': entrenador,
            'info_entrenador': info_entrenador,
        })

def inscribirEquipo(request,id):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@delegacion.com'):
                return redirect('login')
            else:
                return render(request,'RegistrarJugador.html')
        else:
            return redirect('login')
    elif request.method == 'POST':
        print(request.POST)
        nombre = request.POST.get('Nombre')
        apodo = request.POST.get('Apodo')
        posicion = request.POST.get('Posicion')
        dorsal = request.POST.get('Nro_camiseta')
        ci = request.POST.get('Documento')
        fecha = request.POST.get('Fecha_nac')
        telefono = request.POST.get('Telefono')
        foto = request.FILES.get('foto')
        
        id_equipo = Equipo.objects.filter(id=id)
        id_equipo.update(estado_inscripcion_equipo="INSCRITO")

        jugador = Jugador(id_equipo=id_equipo[0],ci_jugador= ci, nacimiento_jugador = fecha,telefono_jugador = telefono, foto_jugador = foto ,nombre_jugador = nombre, apodo_jugador = apodo, posicion_jugador = posicion,dorsal_jugador = dorsal)
        jugador.save()
        messages.success(request, "Jugador registrado correctamente")
        return redirect('delegacionEquipo')

def inscribirEntrenador(request,id):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@delegacion.com'):
                return redirect('login')
            else:
                return render(request,'RegistrarEntrenador.html')
        else:
            return redirect('login')
    elif request.method == 'POST':
        print(request.POST)
        nombre = request.POST.get('Nombre')
        apodo = request.POST.get('Apodo')
        nacionaldiad = request.POST.get('nacionalidad')
        ci = request.POST.get('Documento')
        fecha = request.POST.get('Fecha_nac')
        telefono = request.POST.get('Telefono')
        foto = request.FILES.get('foto')
        
        entrenador = Entrenador(ci_entrenador= ci, nacimiento_entrenador = fecha,telefono_entrenador = telefono, foto_entrenador = foto ,nombre_entrenador = nombre, apodo_entrenador = apodo,nacionalidad_entrenador = nacionaldiad)
        entrenador.save()
        equipo = Equipo.objects.filter(id=id)
        equipo.update(id_entrenador_equipo = entrenador, estado_inscripcion_equipo="INSCRITO")
        messages.success(request, "Entrenador registrado correctamente")
        return redirect('delegacionEquipo')

def torneos(request):
    torneosTerminados = Torneo.objects.filter(torneo_estado=0)
    torneosActual = Torneo.objects.filter(torneo_estado=1)
    return render(request, 'torneos.html', {
         "torneosTerminados": torneosTerminados,
         "torneoActual": torneosActual
    })


def editar_torneo(request,id):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if request.user.email.endswith('@delegacion.com'):
                return redirect('login')
            else:
                torneo = Torneo.objects.filter(id=id)
                preIns = Pre_Inscripcion.objects.filter(id_torneo=id)
                rez = Inscripcion.objects.filter(id_torneo=id)
                return render(request,'editarTorneo.html',{'torneo':torneo[0]
                ,'preIns':preIns[0]
                ,'rez':rez[0]})
        else:
            return redirect('login')
    elif request.method == 'POST':
        print(request.POST)
        print(request.FILES)

        torneo = Torneo.objects.get(id=id)
        torneoPreIns = Pre_Inscripcion.objects.get(id_torneo=id)
        torneoRez = Inscripcion.objects.get(id_torneo=id)
    
        form = TorneoForm(request.POST or None, request.FILES or None,instance = torneo)
        form2 = TorneoPreInsForm(request.POST or None, request.FILES or None,instance = torneoPreIns)
        form3 = TorneoRezForm(request.POST or None, request.FILES or None,instance = torneoRez)

        print(form.is_valid())
        print(form2.is_valid())
        print(form3.is_valid())
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form2.save()
            form3.save()
            messages.success(request, "Información editada correctamente")
            
        else:
            messages.error(request, "Algo salio mal, intente nuevamente")
        return redirect('torneos')

def bajaTorneo(request,id):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            if not request.user.email.endswith('@admin.com'):
                return redirect('login')
            else:
                torneo = Torneo.objects.filter(id=id)
                torneo.update(torneo_estado = 0)
                messages.success(request, "Torneo dado de BAJA")
                return redirect('torneos')
        else:
            return redirect('login')