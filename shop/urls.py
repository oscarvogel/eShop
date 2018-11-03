from django.conf.urls import url

from shop import views

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.detalle_producto,name='detalle_producto'),
    url(r'^(?P<categoria_slug>[-\w]+)/$',views.inicio,name='producto_lista_x_categoria'),
]