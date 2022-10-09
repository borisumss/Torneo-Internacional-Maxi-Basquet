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

class Etapa_Inscripcion(models.Model):
    tipo_inscripcion = models.CharField(max_length=10)
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
    monto_inscripcion = models.DecimalField(max_digits=10, decimal_places=2)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return "%s del %s al %s" % (self.tipo_inscripcion, self.fecha_inicio, self.fecha_fin)

class Categorias_Torneo(models.Model):
    nombre_categoria = models.CharField(max_length=20)
    edad_minima = models.IntegerField()
    edad_maxima = models.IntegerField()
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_categoria
