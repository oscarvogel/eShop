# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-20 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20181020_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenportada',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]