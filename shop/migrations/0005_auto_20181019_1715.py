# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-19 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20181019_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenesproducto',
            name='principal',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='productos/imagenes/%Y/%m/%d'),
        ),
    ]