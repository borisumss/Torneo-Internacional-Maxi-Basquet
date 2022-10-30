# Generated by Django 4.1 on 2022-10-20 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0006_delegado_inscripcion_id_delegadoins_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delegado',
            fields=[
                ('id_delegado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_delegado', models.CharField(max_length=50, null=True)),
                ('ci_delegado', models.CharField(max_length=15, null=True)),
                ('nacimiento_delegado', models.DateField()),
                ('telefono_delegado', models.CharField(max_length=15, null=True)),
                ('foto_delegado', models.ImageField(null=True, upload_to='static/imagenes/equipos/delegados', verbose_name='Foto Delegado')),
            ],
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_entrenador', models.CharField(max_length=50, null=True)),
                ('ci_entrenador', models.CharField(max_length=50, null=True)),
                ('nacimiento_entrenador', models.DateField()),
                ('foto_entrenador', models.ImageField(null=True, upload_to='static/imagenes/equipos/entrenadores/', verbose_name='Foto Enrtenador')),
                ('telefono_entrenador', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.CharField(max_length=50, null=True)),
                ('pais_origen', models.CharField(max_length=50, null=True)),
                ('ciudad_origen', models.CharField(max_length=50, null=True)),
                ('escudo_equipo', models.ImageField(null=True, upload_to='static/imagenes/equipos/escudos/', verbose_name='Escudo equipo')),
                ('portada_equipo', models.ImageField(null=True, upload_to='static/imagenes/equipos/portadas/', verbose_name='Foto equipo')),
                ('categoria_equipo', models.CharField(max_length=50, null=True)),
                ('estado_inscripcion_equipo', models.CharField(max_length=50, null=True)),
                ('id_delegado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.delegado')),
                ('id_entrenador_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.entrenador')),
                ('id_torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.torneo')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_jugador', models.CharField(max_length=50, null=True)),
                ('ci_jugador', models.CharField(max_length=50, null=True)),
                ('nacimiento_jugador', models.DateField()),
                ('foto_jugador', models.ImageField(null=True, upload_to='static/imagenes/equipos/jugadores/', verbose_name='Foto jugador')),
                ('telefono_jugador', models.CharField(max_length=50, null=True)),
                ('dorsal_jugador', models.CharField(max_length=5, null=True)),
                ('posicion_jugador', models.CharField(max_length=50, null=True)),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.equipo')),
            ],
        ),
    ]