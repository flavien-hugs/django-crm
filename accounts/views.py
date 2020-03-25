# -*- coding: utf-8 -*-
# accounts/views.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'


from django.shortcuts import render
from django.http import HttpResponse


# HOME VIEW
def home(request):

    template = 'accounts/dashboard.html'
    return render(request, template)


# HOME PRODUCT
def product(request):

    template = 'accounts/product.html'
    return render(request, template)


# HOME CUSTOMER
def customer(request):

    template = 'accounts/customer.html'
    return render(request, template)