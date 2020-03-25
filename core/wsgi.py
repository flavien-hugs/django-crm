# -*- coding: utf-8 -*-
# core/wsgi.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
