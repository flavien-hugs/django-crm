# -*- coding: utf-8 -*-
# accounts/admin.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'


from django.contrib import admin
from accounts.models import Customer, Product, Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
