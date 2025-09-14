"""
WSGI config for moviesstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""


# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

## assuming your django settings file is at '/home/khayalshah1/mysite/mysite/settings.py'
## and your manage.py is is at '/home/khayalshah1/mysite/manage.py'
path = '/home/khayalshah1/moviesstore'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'moviesstore.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
