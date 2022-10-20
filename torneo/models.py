from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Organizador(models.Model):
    nombre_organizador = models.CharField(max_length=50)
    correo_organizador = models.CharField(max_length=30)
    telefono_organizador = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_organizador
        #return "%s %s" % (self.nombre_organizador, self.telefono_organizador)
    class Meta:
        ordering = ['nombre_organizador']

class Torneo(models.Model):
    nombre_torneo = models.CharField(max_length=50)
    fecha_torneo_inicio = models.DateField(null=True)
    fecha_torneo_fin = models.DateField(null=True)
    pais_torneo = models.CharField(max_length=30)
    torneo_estado = models.BooleanField(default=True)
    invitacion_documento = models.FileField(upload_to='static/imagenes/convocatorias/', verbose_name='Convocatoria')
    logo = models.ImageField(upload_to='static/imagenes/logos/', verbose_name='LogoTorneo', null=True)
    id_organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_torneo
    
    #class Meta:
    #    ordering = ['']

## REVISAR EL CAMPO DE 'DateField, BooleanField si ocurrieran errores'
class Inscripcion(models.Model):
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
    monto_inscripcion = models.DecimalField(max_digits=10, decimal_places=2)
    estado_inscripcion = models.BooleanField(default=False)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return "Rezagados del %s al %s" % (self.fecha_inicio, self.fecha_fin)

class Pre_Inscripcion(models.Model):
    fecha_inicioPre = models.DateField(auto_now=False, auto_now_add=False)
    fecha_finPre = models.DateField(auto_now=False, auto_now_add=False)
    monto_Preinscripcion = models.DecimalField(max_digits=10, decimal_places=2)
    estado_Preinscripcion = models.BooleanField(default=True)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return "Preinscripción del %s al %s" % (self.fecha_inicioPre, self.fecha_finPre)

## REVISAR EL CAMPO DE 'ImageField si ocurrieran errores'
class delegado_Inscripcion(models.Model):
    nombre_delegado_inscripcion = models.CharField(max_length=50)
    estado_delegado_inscripcion = models.CharField(max_length=15)
    correo_delegado_inscripcion = models.CharField(max_length=50)
    ci_delegado_inscripcion = models.CharField(max_length=15)
    telefono_delegado_inscripcion = models.CharField(max_length=15)
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    recibo_inscripcion = models.ImageField(upload_to='static/imagenes/Comprobantes/', verbose_name='Recibo Rezagados', null=True)
    id_delegadoIns = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class delegado_PreInscripcion(models.Model):
    nombre_delegado_Preinscripcion = models.CharField(max_length=50)
    estado_delegado_Preinscripcion = models.CharField(max_length=15)#Estados: ACEPTADO, RECHAZADO, PENDIENTE, BAJA
    correo_delegado_Preinscripcion = models.CharField(max_length=50)
    ci_delegado_Preinscripcion = models.CharField(max_length=15)
    telefono_delegado_Preinscripcion = models.CharField(max_length=15)
    id_Pre_inscripcion = models.ForeignKey(Pre_Inscripcion, on_delete=models.CASCADE)
    recibo_Preinscripcion = models.ImageField(upload_to='static/imagenes/Comprobantes/', verbose_name='Recibo Preinscripción', null=True)
    id_delegadoPreIns = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Categorias_Torneo(models.Model):
    nombre_categoria = models.CharField(max_length=20)
    edad_minima = models.IntegerField()
    edad_maxima = models.IntegerField()
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_categoria

class Delegado(models.Model):
    id_delegado = models.IntegerField(primary_key=True)
    nombre_delegado = models.CharField(max_length=50, null=True)
    ci_delegado = models.CharField(max_length=15, null=True)
    nacimiento_delegado = models.DateField(auto_now=False, auto_now_add=False)
    telefono_delegado = models.CharField(max_length=15, null=True)
    foto_delegado = models.ImageField(upload_to='static/imagenes/equipos/delegados', verbose_name='Foto Delegado', null=True)

class Entrenador(models.Model):
    nombre_entrenador = models.CharField(max_length=50, null=True)
    ci_entrenador = models.CharField(max_length=50, null=True)
    nacimiento_entrenador = models.DateField(auto_now=False, auto_now_add=False)
    foto_entrenador =  models.ImageField(upload_to='static/imagenes/equipos/entrenadores/', verbose_name='Foto Enrtenador', null=True)
    telefono_entrenador = models.CharField(max_length=50, null=True)

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=50, null=True)
    pais_origen = models.CharField(max_length=50, null=True)
    ciudad_origen = models.CharField(max_length=50, null=True)
    escudo_equipo =  models.ImageField(upload_to='static/imagenes/equipos/escudos/', verbose_name='Escudo equipo', null=True)
    portada_equipo =  models.ImageField(upload_to='static/imagenes/equipos/portadas/', verbose_name='Foto equipo', null=True)
    categoria_equipo = models.CharField(max_length=50, null=True)
    estado_inscripcion_equipo = models.CharField(max_length=50,null=True)

    id_delegado = models.ForeignKey(Delegado, on_delete=models.CASCADE)
    id_entrenador_equipo = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    

class Jugador(models.Model):
    nombre_jugador = models.CharField(max_length=50, null=True)
    ci_jugador = models.CharField(max_length=50, null=True)
    nacimiento_jugador = models.DateField(auto_now=False, auto_now_add=False)
    foto_jugador =  models.ImageField(upload_to='static/imagenes/equipos/jugadores/', verbose_name='Foto jugador', null=True)
    telefono_jugador = models.CharField(max_length=50, null=True)
    dorsal_jugador = models.CharField(max_length=5, null=True)
    posicion_jugador = models.CharField(max_length=50, null=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)