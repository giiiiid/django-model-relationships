from django.shortcuts import render, HttpResponse
from .models import *
from django.db.models import Q

def orders(request):
    customers = Customer.objects.all()

    orders = Order.objects.all()

    # delivery = orders.filter(delivery='Delivery').count()
    jollof = Order.objects.filter(food=3)
    context = {'customers':customers, 'orders':orders, 'jollof':jollof}
    return render(request, 'orders.html', context)


def customers(request, name):
    customer = Customer.objects.get(name=name)
    
    orders = customer.order_set.all()
    # total = 
    return render(request, 'customers.html', context)