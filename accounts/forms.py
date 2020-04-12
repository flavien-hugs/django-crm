# -*- coding: utf-8 -*-
# accounts/forms.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__ = '0.0.1'
__copyright__ = '© 2019 unsta'

from django.forms import ModelForm

from accounts.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
