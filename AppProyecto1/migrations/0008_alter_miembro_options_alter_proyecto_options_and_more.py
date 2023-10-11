# Generated by Django 4.2.5 on 2023-10-10 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto1', '0007_proyecto_fechadecreacion_proyecto_imagen_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miembro',
            options={'default_permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='proyecto',
            options={'default_permissions': ()},
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='miembro',
        ),
        migrations.AlterField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppProyecto1.proyecto'),
        ),
    ]
