# -*- coding: utf-8 -*-
# accounts/urls.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'


from django.urls import path
from accounts.views import product, customer, createOrder, updateOrder, deleteOrder

app_name = 'accounts'

urlpatterns = [
    # url 'product/'
    path('product/', product, name='product'),
    # url 'customer/<str:pk>/'
    path('customer/<str:pk>/', customer, name='customer'),
    # url 'create-order/'
    path('create-order/', createOrder, name='create-order'),
    # url 'update-order/<str:pk>/'
    path('update-order/<str:pk>/', updateOrder, name='update-order'),
    # url 'delete-order/<str:pk>/'
    path('delete-order/<str:pk>/', deleteOrder, name='delete-order')
]
