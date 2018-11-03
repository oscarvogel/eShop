# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-20 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20181019_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenPortada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=80)),
                ('imagen', models.ImageField(upload_to='portada/%Y/%m/%d')),
            ],
            options={
                'ordering': ('descripcion',),
                'db_table': 'imagenportada',
            },
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='media/productos/imagenes/%Y/%m/%d'),
        ),
    ]