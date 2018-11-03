"""electro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from shop import views
from shop.views import inicio

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^accounts/login/$', login, {'template_name': 'admin/login.html'}, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^ordenes/', include('orders.urls', namespace='ordenes')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
