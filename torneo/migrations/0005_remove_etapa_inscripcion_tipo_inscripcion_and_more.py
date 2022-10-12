# Generated by Django 4.1 on 2022-10-11 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0004_torneo_logo_alter_torneo_invitacion_documento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etapa_inscripcion',
            name='tipo_inscripcion',
        ),
        migrations.CreateModel(
            name='Etapa_PreInscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicioPre', models.DateField()),
                ('fecha_finPre', models.DateField()),
                ('monto_Preinscripcion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.torneo')),
            ],
        ),
        migrations.CreateModel(
            name='delegado_PreInscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_delegado_Preinscripcion', models.CharField(max_length=50)),
                ('estado_delegado_Preinscripcion', models.CharField(max_length=15)),
                ('correo_delegado_Preinscripcion', models.CharField(max_length=30)),
                ('ci_delegado_Preinscripcion', models.CharField(max_length=15)),
                ('telefono_delegado_Preinscripcion', models.CharField(max_length=15)),
                ('recibo_Preinscripcion', models.ImageField(null=True, upload_to='static/imagenes/Comprobantes/', verbose_name='Recibo Preinscripción')),
                ('id_etapa_Preinscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.etapa_preinscripcion')),
            ],
        ),
        migrations.CreateModel(
            name='delegado_Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_delegado_inscripcion', models.CharField(max_length=50)),
                ('estado_delegado_inscripcion', models.CharField(max_length=15)),
                ('correo_delegado_inscripcion', models.CharField(max_length=30)),
                ('ci_delegado_inscripcion', models.CharField(max_length=15)),
                ('telefono_delegado_inscripcion', models.CharField(max_length=15)),
                ('recibo_inscripcion', models.ImageField(null=True, upload_to='static/imagenes/Comprobantes/', verbose_name='Recibo Rezagados')),
                ('id_etapa_inscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.etapa_inscripcion')),
            ],
        ),
    ]