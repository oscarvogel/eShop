# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#import weasyprint
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

from cart.cart import Cart
from orders.forms import OrdenCreateForm
from orders.models import OrdenDetalle, Orden


def crear_orden(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrdenCreateForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            user = User.objects.get(username=request.user.username)
            orden.usuario = user
            orden.save()
            for item in cart:
                OrdenDetalle.objects.create(
                    orden = orden,
                    producto = item['product'],
                    precio = item['price'],
                    cantidad = item['quantity']
                )
            #limpiamos el carrito
            cart.clear()
            return render(request,
                          'ordenes/orden/creada.html',
                          {'orden': orden})
    else:
        form = OrdenCreateForm()
    return render(request,
                  'ordenes/orden/crear.html',
                  {'cart': cart, 'form': form})

@staff_member_required
def admin_orden_detalle(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id)
    return render(request,'admin/ordenes/orden/detalle.html',{
        'orden': orden
    })

@staff_member_required
def admin_orden_pdf(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id)
    html = render_to_string('ordenes/orden/pdf.html',{'orden': orden})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\"orden_{}.pdf"'.format(orden.id)
    #weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response