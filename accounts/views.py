# -*- coding: utf-8 -*-
# accounts/views.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'


from django.shortcuts import render, redirect
from django.http import HttpResponse

from accounts.forms import OrderForm
from accounts.models import Customer, Product, Order


# HOME VIEW
def home(request):
    page_title = 'dashboard'
    all_orders = Order.objects.all()
    total_orders = all_orders.count()
    delivered = all_orders.filter(status='Delivery').count()
    pending = all_orders.filter(status='Pending').count()

    all_customers = Customer.objects.all()
    total_customers = all_customers.count()

    context = {
        'title': page_title,
        'orders': all_orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'customers': all_customers,
        'total_customers': total_customers
    }
    template = 'accounts/dashboard.html'
    return render(request, template, context)


# HOME PRODUCT
def product(request):
    page_title = 'tous les produits'
    all_products = Product.objects.all()

    context = {'title': page_title, 'products': all_products}
    template = 'accounts/product.html'

    return render(request, template, context)


# HOME CUSTOMER
def customer(request, pk):
    page_title = 'customer'
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {
        'title': page_title,
        'customer': customer,
        'orders': orders,
        'order_count': order_count
    }
    template = 'accounts/customer.html'
    return render(request, template, context)


# HOME CREATE ORDER
def createOrder(request):
    page_title = 'create order'
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }

    template = 'partials/order_form.html'
    return render(request, template, context)


# HOME CREATE UPDATE ORDER
def updateOrder(request, pk):
    page_title = 'mise à jour'
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': page_title,
        'form': form
    }
    
    template = 'partials/order_form.html'
    return render(request, template, context)


# HOME CREATE DELETE ORDER
def deleteOrder(request, pk):
    page_title = 'delete'
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'title': page_title,
        'item': order
    }
    
    template = 'partials/delete.html'
    return render(request, template, context)