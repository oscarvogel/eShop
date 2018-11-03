# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from electro import settings
from shop.models import Producto, Categoria, ImagenesProducto, ArchivosProducto, ImagenPortada

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

admin.site.register(Categoria, CategoriaAdmin)

class ImagenesInline(admin.TabularInline):
    model = ImagenesProducto

class ArchivosInline(admin.TabularInline):
    model = ArchivosProducto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'precio', 'stock', 'disponible', 'codigociber', 'actualizado']
    list_filter = ['disponible', 'creado', 'actualizado']
    list_editable = ['precio', 'stock', 'disponible', 'codigociber']
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ['nombre','codigociber']
    inlines = [
        ImagenesInline,
        ArchivosInline
    ]

admin.site.register(Producto, ProductoAdmin)

class ImagenPortadaAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'imagen']

admin.site.register(ImagenPortada, ImagenPortadaAdmin)

admin.site.site_header = settings.NOMBRE_SITIO
