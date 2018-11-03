# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from cart.forms import CartAddProductForm
from electro import settings
from shop.forms import BusquedaForm, ContactoForm
from shop.models import Categoria, Producto, ImagenPortada


@login_required
def inicio(request, categoria_slug=None):
    categorias = None
    categoria = None
    productos = None
    imgportada = ImagenPortada.objects.filter(activo=True)
    context = {'titulo_principal': settings.TITULO_PRINCIPAL,
               'nombre_sitio':settings.NOMBRE_SITIO,
               'web_empresa':settings.WEB_EMPRESA}
    if request.method == "POST":
        form = BusquedaForm(request.POST)
        busqueda = True
        if form.is_valid():
            formdata = form.cleaned_data
            categorias = Categoria.objects.all()
            productos = Producto.objects.filter(nombre__icontains=formdata['busqueda']) | \
                Producto.objects.filter(codigociber__icontains=formdata['busqueda'])
    else:
        busqueda = False
        form = BusquedaForm()
        categoria = None
        categorias = Categoria.objects.all()
        productos = Producto.objects.all()
        if categoria_slug:
            categoria = get_object_or_404(Categoria, slug=categoria_slug)
            productos = productos.filter(categoria=categoria)[:6]
        else:
            productos = productos[:6]


    return render(request, 'index.html',{
        'categorias':categorias,
        'productos':productos,
        'categoria':categoria,
        'form':form,
        'imgportada':imgportada,
        'busqueda':busqueda,
        'context':context
    })

def detalle_producto(request, id, slug):
    categorias = None
    categorias = Categoria.objects.all()
    producto = get_object_or_404(Producto,id=id,slug=slug,disponible=True)

    cart_product_form = CartAddProductForm()
    return render(request,'shop/producto/detalle.html',{
        'producto': producto,
        'categorias': categorias,
        'cart_product_form':cart_product_form
    })

def contacto(request):
    form_class = ContactoForm()

    return render(request, 'base/contacto.html', {
        'form': form_class,
    })

def producto_lista_x_categoria(request):
    pass