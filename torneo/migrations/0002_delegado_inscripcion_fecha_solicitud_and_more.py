# Generated by Django 4.1 on 2022-11-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegado_inscripcion',
            name='fecha_solicitud',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='delegado_preinscripcion',
            name='fecha_solicitud',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]