"""
WSGI config for electro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('C:/Users/oscar/Bitnami Django Stack projects/electro')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:/Users/oscar/Bitnami Django Stack projects/electro/egg_cache")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electro.settings")

application = get_wsgi_application()
