# Generated by Django 2.1.1 on 2018-10-19 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesApp', '0009_pedido_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantes',
            name='correo',
            field=models.EmailField(max_length=255),
        ),
    ]
