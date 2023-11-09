from django.shortcuts import render, HttpResponse
from .models import *
from django.db.models import Q

def orders(request):
    customers = Customer.objects.all()

    orders = Order.objects.all()

    # delivery = orders.filter(delivery='Delivery').count()
   
    context = {'customers':customers, 'orders':orders}
    return render(request, 'orders.html', context)


def customers(request, name):
    customer = Customer.objects.get(name=name)

    orders = customer.order_set.all()
    total = sum([i.food.price for i in orders])

    # total = sum(all_prices)
    context = {'orders':orders, 'total':total}
    return render(request, 'customers.html', context)


def foods(request):
    all_foods = Food.objects.all()
    num_of_orders = Food.objects.all()

    context = {'foods':all_foods, 'orders':num_of_orders}
    return render(request, 'foods.html', context)