# Generated by Django 5.0.6 on 2024-07-01 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agregado',
        ),
        migrations.RemoveField(
            model_name='cafetam',
            name='codCafe',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='cargo',
        ),
        migrations.DeleteModel(
            name='Catalogos',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='comuna',
            name='id_provincia',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_comuna',
        ),
        migrations.RemoveField(
            model_name='sucursal',
            name='id_comuna',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='rut_persona',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='codFormaPago',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='rut',
        ),
        migrations.DeleteModel(
            name='Postres',
        ),
        migrations.RemoveField(
            model_name='provincia',
            name='id_region',
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
        migrations.DeleteModel(
            name='Tamanio',
        ),
        migrations.DeleteModel(
            name='Cafe',
        ),
        migrations.DeleteModel(
            name='CafeTam',
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='Comuna',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='Sucursal',
        ),
        migrations.DeleteModel(
            name='FormaPago',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.DeleteModel(
            name='Provincia',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]