# Generated by Django 4.1 on 2022-10-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0002_alter_categorias_torneo_nombre_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='invitacion_documento',
            field=models.FileField(upload_to='static/imagenes/', verbose_name='Convocatoria'),
        ),
    ]
