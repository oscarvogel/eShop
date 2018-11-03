# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from shop.models import Producto


class Orden(models.Model):

    usuario = models.ForeignKey(User)
    domicilio = models.CharField(max_length=80, default='')
    cp = models.CharField(max_length=10, verbose_name='Codigo Postal', default='')
    telefono = models.CharField(max_length=80, verbose_name='Telefono', default='')
    creada = models.DateTimeField(auto_now_add=True)
    modificada = models.DateTimeField(auto_now=True)
    pagada = models.BooleanField(default=False)

    class Meta:
        ordering = ('-creada',)

    def __str__(self):
        return 'Orden {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrdenDetalle(models.Model):

    orden = models.ForeignKey(Orden, related_name='items')
    producto = models.ForeignKey(Producto, related_name='orden_item')
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.precio * self.cantidad