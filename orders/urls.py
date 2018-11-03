from django.conf.urls import url

from orders import views

urlpatterns = [
    url(r'^crear/$',views.crear_orden, name='crear_orden'),
    url(r'^admin/orden/(?P<orden_id>\d+)/$',views.admin_orden_detalle, name='admin_orden_detalle'),
]