# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181024_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='telefono',
            field=models.CharField(default='', max_length=80, verbose_name='Telefono'),
        ),
    ]