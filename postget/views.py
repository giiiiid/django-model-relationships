from django.shortcuts import render, HttpResponse
from .models import *
from django.db.models import Q

def orders(request):
    # jollof = []
    # for jollof_orders in Order.objects.all():
    #     if 'ollof'.casefold() in jollof_orders.food.name:
    #         jollof.append(jollof_orders)
    
    # for i in jollof:
    #     context = {'i':i}

    orders = Order.objects.first()
    personName = orders.customer_name.name
    personFood = orders.food.name

    customer = Customer.objects.first()
    ordered_items = customer.order_set.all()

    context = {'personFood':personFood, 'personName':personName, 'ordered_items':ordered_items}
    return render(request, 'orders.html', context)