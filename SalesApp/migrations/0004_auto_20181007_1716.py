# Generated by Django 2.1.1 on 2018-10-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesApp', '0003_restaurantes_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantes',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
