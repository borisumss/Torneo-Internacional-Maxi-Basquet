# Generated by Django 4.1 on 2022-10-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias_torneo',
            name='nombre_categoria',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='organizador',
            name='nombre_organizador',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='organizador',
            name='telefono_organizador',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='nombre_torneo',
            field=models.CharField(max_length=50),
        ),
    ]
