# -*- coding: utf-8 -*-
# accounts/urls.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'


from django.urls import path
from accounts.views import product, customer

app_name = 'accounts'

urlpatterns = [
    # url 'product/'
    path('product/', product, name='product'),

    # url 'customer/'
    path('customer/', customer, name='customer'),
]
