from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Q
# from .serializers import *
from .models import (Customer, Tag, 
                    Food, Order)
from .forms import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import json

def orders(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    
    num_of_delivery = Order.objects.filter(delivery='Delivery')
    num_of_pickups = Order.objects.filter(delivery='Pick up')
    delivery_foods = [i.food.name for i in num_of_delivery]
    pickup_foods = [i.food.name for i in num_of_pickups]
    
    orders_api_url = 'http://127.0.0.1:8000/postget/api'
    response = requests.get(orders_api_url).json()
    
    
    # with open('orders.json', 'w') as f:
    #     json.dump(response, f, indent=2)


    context = {'customers':customers, 'orders':orders,
                'delivery':num_of_delivery, 'pickups':num_of_pickups,
                'delivery_foods':delivery_foods, 'pickup_foods':pickup_foods
            }

    return render(request, 'orders.html', context)


def customers(request, name):
    customer = Customer.objects.get(name=name)
    orders = customer.order_set.all()
    total = sum([i.food.price for i in orders])

    context = {'orders':orders, 'total':total, 'customer':customer}
    return render(request, 'customers.html', context)


def foods(request):
    all_foods = Food.objects.all()
    # getting the number of orders for a food in a menu
    num_of_orders = [i.order_set.all().count() for i in all_foods]
    for i,j in enumerate(num_of_orders):
        print(j)

    context = {'foods':all_foods, 'orders':orders}
    return render(request, 'foods.html', context)


def create_order(request, name):
    customer = Customer.objects.get(name=name)
    forms = OrderForms(initial={'customer_name':customer})

    instance_model = customer
    if request.method == 'POST':
        forms = OrderForms(request.POST)
        if forms.is_valid:
            forms.save()
            # return redirect(reverse('customers', kwargs={'instance':str(customer)}))
            # return redirect('/customer')
    context = {'forms':forms, 'customer':customer}
    return render(request, 'place_order.html', context)


# @api_view(['GET','POST'])
# def api(request):
#     orders = Order.objects.all()
#     serializer = OrderSerializer(orders, many=True)
#     return JsonResponse(serializer.data, safe=False)
