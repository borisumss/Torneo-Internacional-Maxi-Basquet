from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from qr_code import qrcode
from PIL import Image
from django.utils import timezone

import torneo
# Create your models here.


class Organizador(models.Model):
    nombre_organizador = models.CharField(max_length=50)
    correo_organizador = models.CharField(max_length=30)
    telefono_organizador = models.CharField(max_length=15)

    def __str__(self):
        return str(self.pk) + "-" + self.nombre_organizador
        # return "%s %s" % (self.nombre_organizador, self.telefono_organizador)

    class Meta:
        verbose_name_plural = "Organizadores"


class Torneo(models.Model):
    nombre_torneo = models.CharField(max_length=50)
    fecha_torneo_inicio = models.DateField(null=True)
    fecha_torneo_fin = models.DateField(null=True)
    pais_torneo = models.CharField(max_length=30)
    torneo_estado = models.BooleanField(default=True)
    invitacion_documento = models.FileField(
        upload_to='static/imagenes/convocatorias/', verbose_name='Convocatoria')
    logo = models.ImageField(
        upload_to='static/imagenes/logos/', verbose_name='LogoTorneo', null=True)
    id_organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + "-" + self.nombre_torneo

    class Meta:
        verbose_name_plural = "Torneos"
    # class Meta:
    #    ordering = ['']

# REVISAR EL CAMPO DE 'DateField, BooleanField si ocurrieran errores'


class Inscripcion(models.Model):
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
    monto_inscripcion = models.DecimalField(max_digits=10, decimal_places=2)
    qr_inscripcion = models.ImageField(
        upload_to='static/imagenes/qrs/', verbose_name='qr2', null=True)
    estado_inscripcion = models.BooleanField(default=False)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + "-" + "Rezagados del %s al %s" % (self.fecha_inicio, self.fecha_fin)

    class Meta:
        verbose_name_plural = "Inscripcion"


class Pre_Inscripcion(models.Model):
    fecha_inicioPre = models.DateField(auto_now=False, auto_now_add=False)
    fecha_finPre = models.DateField(auto_now=False, auto_now_add=False)
    monto_Preinscripcion = models.DecimalField(max_digits=10, decimal_places=2)
    qr_Preinscripcion = models.ImageField(
        upload_to='static/imagenes/qrs/', verbose_name='qr1', null=True)
    estado_Preinscripcion = models.BooleanField(default=True)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + "-" + "Preinscripción del %s al %s" % (self.fecha_inicioPre, self.fecha_finPre)

    class Meta:
        verbose_name_plural = "Preinscripcion"

# REVISAR EL CAMPO DE 'ImageField si ocurrieran errores'


class delegado_Inscripcion(models.Model):
    nombre_delegado_inscripcion = models.CharField(max_length=50)
    estado_delegado_inscripcion = models.CharField(max_length=15)
    correo_delegado_inscripcion = models.CharField(max_length=50)
    ci_delegado_inscripcion = models.CharField(max_length=15)
    telefono_delegado_inscripcion = models.CharField(max_length=15)
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    recibo_inscripcion = models.ImageField(
        upload_to='static/imagenes/Comprobantes/', verbose_name='Recibo Rezagados', null=True)
    fecha_solicitud = models.DateTimeField(default=timezone.now)
    id_delegadoIns = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.pk) + "-" + self.nombre_delegado_inscripcion

    class Meta:
        verbose_name_plural = "Delegado inscripciones"


class delegado_PreInscripcion(models.Model):
    nombre_delegado_Preinscripcion = models.CharField(max_length=50)
    # Estados: ACEPTADO, RECHAZADO, PENDIENTE, BAJA
    estado_delegado_Preinscripcion = models.CharField(max_length=15)
    correo_delegado_Preinscripcion = models.CharField(max_length=50)
    ci_delegado_Preinscripcion = models.CharField(max_length=15)
    telefono_delegado_Preinscripcion = models.CharField(max_length=15)
    id_Pre_inscripcion = models.ForeignKey(
        Pre_Inscripcion, on_delete=models.CASCADE)
    recibo_Preinscripcion = models.ImageField(
        upload_to='static/imagenes/Comprobantes/', verbose_name='Recibo Preinscripción', null=True)
    fecha_solicitud = models.DateTimeField(default=timezone.now)
    id_delegadoPreIns = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.pk) + "-" + self.nombre_delegado_Preinscripcion

    class Meta:
        verbose_name_plural = "Delegado preinscripciones"


class Categorias_Torneo(models.Model):
    nombre_categoria = models.CharField(max_length=20)
    edad_minima = models.IntegerField()
    edad_maxima = models.IntegerField()
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + "-" + "%s [%s-%s] " % (self.nombre_categoria, self.edad_minima, self.edad_maxima)

    class Meta:
        verbose_name_plural = "Categorias de torneo"


class Delegado(models.Model):
    id_delegado = models.IntegerField(primary_key=True)
    nombre_delegado = models.CharField(max_length=50, null=True)
    ci_delegado = models.CharField(max_length=15, null=True)
    nacimiento_delegado = models.DateField(
        auto_now=False, auto_now_add=False, null=True)
    telefono_delegado = models.CharField(max_length=15, null=True)
    foto_delegado = models.ImageField(
        upload_to='static/imagenes/equipos/delegados', verbose_name='Foto Delegado', null=True)

    def save(self, *args, **kwargs):
        super(Delegado, self).save(*args, **kwargs)
        if self.foto_delegado:
            print(self.foto_delegado)
            imag = Image.open(self.foto_delegado.path)
            if imag.width > 200 or imag.height > 200:
                output_size = (200, 200)
                imag.thumbnail(output_size)
                imag.save(self.foto_delegado.path)

    def __str__(self):
        return str(self.pk) + "-" + self.nombre_delegado

    class Meta:
        verbose_name_plural = "Delegados"


class Entrenador(models.Model):
    nombre_entrenador = models.CharField(max_length=50, null=True)
    apodo_entrenador = models.CharField(max_length=50, null=True)
    nacionalidad_entrenador = models.CharField(max_length=50, null=True)
    ci_entrenador = models.CharField(max_length=50, null=True)
    nacimiento_entrenador = models.DateField(
        auto_now=False, auto_now_add=False)
    foto_entrenador = models.ImageField(
        upload_to='static/imagenes/equipos/entrenadores/', verbose_name='Foto Enrtenador', null=True)
    telefono_entrenador = models.CharField(max_length=50, null=True)

    def save(self, *args, **kwargs):
        super(Entrenador, self).save(*args, **kwargs)
        print(self.foto_entrenador)
        imag = Image.open(self.foto_entrenador.path)
        if imag.width > 200 or imag.height > 200:
            output_size = (200, 200)
            imag.thumbnail(output_size)
            imag.save(self.foto_entrenador.path)

    def __str__(self):
        return str(self.pk) + "-" + self.nombre_entrenador

    class Meta:
        verbose_name_plural = "Entrenadores"


class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=50, null=True)
    pais_origen = models.CharField(max_length=50, null=True)
    ciudad_origen = models.CharField(max_length=50, null=True)
    escudo_equipo = models.ImageField(
        upload_to='static/imagenes/equipos/escudos/', verbose_name='Escudo equipo', null=True)
    portada_equipo = models.ImageField(
        upload_to='static/imagenes/equipos/portadas/', verbose_name='Foto equipo', null=True)
    categoria_equipo = models.CharField(max_length=50, null=True)
    estado_inscripcion_equipo = models.CharField(max_length=50, null=True)
    id_delegado = models.ForeignKey(
        Delegado, on_delete=models.CASCADE, null=True)
    id_entrenador_equipo = models.ForeignKey(
        Entrenador, on_delete=models.CASCADE, null=True)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        super(Equipo, self).save(*args, **kwargs)
        print(self.escudo_equipo)
        if self.escudo_equipo:
            imag = Image.open(self.escudo_equipo.path)
            if imag.width > 200 or imag.height > 200:
                output_size = (200, 200)
                imag.thumbnail(output_size)
                imag.save(self.escudo_equipo.path)


    def __str__(self):
        if self.nombre_equipo:
            return str(self.id) + "-" + self.nombre_equipo
        else:
            return str(self.id)

    class Meta:
        verbose_name_plural = "Equipos"


class Jugador(models.Model):
    nombre_jugador = models.CharField(max_length=50, null=True)
    apodo_jugador = models.CharField(max_length=50, null=True)
    ci_jugador = models.CharField(max_length=50, null=True)
    nacimiento_jugador = models.DateField(auto_now=False, auto_now_add=False)
    foto_jugador = models.ImageField(
        upload_to='static/imagenes/equipos/jugadores/', verbose_name='Foto jugador', null=True)
    telefono_jugador = models.CharField(max_length=50, null=True)
    dorsal_jugador = models.CharField(max_length=5, null=True)
    posicion_jugador = models.CharField(max_length=50, null=True)
    faltas = models.IntegerField(null=True)
    anotaciones = models.IntegerField(null=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Jugador, self).save(*args, **kwargs)
        print(self.foto_jugador)
        imag = Image.open(self.foto_jugador.path)
        if imag.width > 200 or imag.height > 200:
            output_size = (200, 200)
            imag.thumbnail(output_size)
            imag.save(self.foto_jugador.path)

    def __str__(self):
        return str(self.pk) + "-" + self.nombre_jugador

    class Meta:
        verbose_name_plural = "Jugadores"


class Tabla_posiciones(models.Model):
    id_equipo = models.IntegerField(primary_key=True)
    nombre_equipo = models.CharField(max_length=50, null=True)
    escudo_equipo = models.ImageField(
        upload_to='static/imagenes/equipos/escudos/', verbose_name='Escudo equipo', null=True)
    categoria_equipo = models.CharField(max_length=50, null=True)
    partidos_jugados = models.IntegerField(null=True)
    partidos_ganados = models.IntegerField(null=True)
    partidos_perdidos = models.IntegerField(null=True)
    puntos_favor = models.IntegerField(null=True)
    puntos_encontra = models.IntegerField(null=True)
    diferencia = models.IntegerField(null=True)
    puntaje_total = models.IntegerField(null=True)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + "-" + self.nombre_equipo

    class Meta:
        verbose_name_plural = "Tabla de posiciones"
# @receiver(post_save, sender=Jugador)
# def create_qr(sender, instance, **kwargs):
#     code = instance.ci_jugador
#     img = qrcode.make(code)
#     instance.qr_path = img
#     print(img)
#    #instance.save()


class Enfrentamiento(models.Model):
    equipo_a = models.CharField(max_length=50, null=True)
    puntajeEquipoA = models.IntegerField(null=True)
    escudo_equipoA = models.ImageField(
        upload_to='static/imagenes/equipos/escudos/', verbose_name='Escudo equipo', null=True)
    equipo_b = models.CharField(max_length=50, null=True)
    puntajeEquipoB = models.IntegerField(null=True)
    escudo_equipoB = models.ImageField(
        upload_to='static/imagenes/equipos/escudos/', verbose_name='Escudo equipo', null=True)
    fecha_enfrentamiento = models.DateTimeField(
        auto_now=False, auto_now_add=True, null=True)
    categoria = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + "-" + self.equipo_a + "vs" + self.equipo_b

    class Meta:
        verbose_name_plural = "Enfrentamientos"


class Estadisticas_enfrentamiento(models.Model):
    faltas = models.IntegerField(null=True)
    anotaciones = models.IntegerField(null=True)
    id_jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    id_enfrentamiento = models.ForeignKey(Enfrentamiento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + "-" + self.faltas + "-" + self.anotaciones

    class Meta:
        verbose_name_plural = "Estadisticas de enfrentamientos"
