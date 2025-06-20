"""
WSGI config for realestate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

path = '/home//Miteshptl/realestate'
if path not in sys.path:
  sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')

application = get_wsgi_application()
