# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
import datetime

from django.contrib import admin

# Register your models here.
from django.http import HttpResponse
from django.urls import reverse

from orders.models import OrdenDetalle, Orden

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Exportar a CSV'

def detalle_orden(obj):
    return '<a href="{}" >Ver</a>'.format(reverse('ordenes:admin_orden_detalle', args=[obj.id]))

detalle_orden.allow_tags = True

class OrdenItemInline(admin.TabularInline):
    model = OrdenDetalle
    raw_id_fields = ['producto']

class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'domicilio', 'cp', 'creada', 'modificada', 'pagada', detalle_orden]
    list_filter = ['pagada', 'creada', 'modificada']
    inlines = [OrdenItemInline]
    raw_id_fields = ['usuario']
    actions = [export_to_csv]

admin.site.register(Orden, OrdenAdmin)