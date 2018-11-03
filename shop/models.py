# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse


class Categoria(models.Model):

    nombre = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('shop:producto_lista_x_categoria',args=[self.slug])

class Producto(models.Model):
    categoria = models.ManyToManyField(Categoria, related_name='productos')
    nombre = models.CharField(max_length=200, db_index=True)
    codigociber = models.CharField(max_length=30, default='', verbose_name='Codigo CiberService')
    slug = models.SlugField(max_length=200, db_index=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=12, decimal_places=3)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='media/productos/imagenes/%Y/%m/%d', blank=True)
    etiquetas = models.CharField(max_length=200, default='', blank=True)

    class Meta:
        db_table = "producto"
        ordering = ('nombre',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return "{}".format(bytearray(self.nombre, 'latin-1', errors='ignore').decode('utf-8','ignore'))

    def get_absolute_url(self):
        return reverse('shop:detalle_producto',
                       args=[self.id, self.slug])

class ImagenesProducto(models.Model):

    descripcion = models.CharField(max_length=80)
    producto = models.ForeignKey(Producto, related_name='imgprod', on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to='productos/imagenes/%Y/%m/%d', blank=True)

    class Meta:
        db_table = "imagenprod"
        ordering = ('producto',)

    def __str__(self):
        return self.descripcion

class ArchivosProducto(models.Model):

    descripcion = models.CharField(max_length=80)
    producto = models.ForeignKey(Producto, related_name='archprod', on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to='productos/archivos/%Y/%m/%d', blank=True)

    class Meta:
        db_table = "archivoprod"
        ordering = ('producto',)

    def __str__(self):
        return self.descripcion


class ImagenPortada(models.Model):

    descripcion = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='portada/%Y/%m/%d')
    activo = models.BooleanField(default=False)

    class Meta:
        db_table = "imagenportada"
        ordering = ('descripcion',)

    def __str__(self):
        return self.descripcion