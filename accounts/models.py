# -*- coding: utf-8 -*-
# accounts/models.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'


from django.db import models
from django.urls import reverse

# MODELS DATABASES : CUSTOMER
class Customer(models.Model):
    name = models.CharField('Nom', max_length=50, null=True)
    phone = models.CharField('Téléphone', max_length=10, null=True)
    email = models.EmailField('Email', null=True)
    date_created = models.DateTimeField('Date de création', auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Customer'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accounts:customer', args=[self.id])

# MODELS DATABASES : TAG
class Tag(models.Model):
    name = models.CharField('Categorie', max_length=200, null=True)
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categorie'


# MODELS DATABASES : PRODUIT
class Product(models.Model):
    CATEGORIES = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField('Nom du produit', max_length=200, null=True)
    price = models.FloatField('Prix du produit', null=True)
    category = models.CharField('Categorie du produit', choices=CATEGORIES, max_length=200, null=True)
    description = models.CharField('Description du produit', max_length=200, null=True, blank=True)
    date_created = models.DateTimeField("Date d'ajout", auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='categorie')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Produit'


# MODELS DATABASES : ORDER
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivery', 'Delivery'),
    )
    
    customer = models.ForeignKey(Customer, verbose_name='customer', null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name='produit', null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField("Date d'ajout", auto_now_add=True, null=True)
    status = models.CharField('Status', choices=STATUS, max_length=200, null=True)

    class Meta:
        verbose_name='Order'

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse('accounts:update-order', args=[self.id])
