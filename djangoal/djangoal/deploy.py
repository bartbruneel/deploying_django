"""
WSGI config for djangoal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys


from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise

path=/"home/bartbruneel1/deploying_django/djangoal"
if path not in sys.path:
	sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoal.settings")

application = get_wsgi_application()
application=DjangoWhiteNoise(application)
