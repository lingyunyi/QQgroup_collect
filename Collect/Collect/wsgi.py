"""
WSGI config for Collect project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append(r'C:\PythonProject\Collect\Collect')
sys.path.append(r'C:\PythonProject\Collect')
sys.path.append(r'C:\PythonProject\static')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Collect.settings')

application = get_wsgi_application()
