from django.shortcuts import render, HttpResponse
from .models import *
from django.db.models import Q

def orders(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    
    num_of_delivery = Order.objects.filter(delivery='Delivery')
    num_of_pickups = Order.objects.filter(delivery='Pick up')
    
    delivery_foods = [i.food.name for i in num_of_delivery]
    pickup_foods = [i.food.name for i in num_of_pickups]
    

    context = {'customers':customers, 'orders':orders,
                'delivery':num_of_delivery, 'pickups':num_of_pickups,
                'delivery_foods':delivery_foods, 'pickup_foods':pickup_foods
    }
    
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
    # num_of_orders = Food.order_set.all()
    # num_of_orders = {}

    # for num in Food.order_set:
    #     if num.name in num_of_orders:
    #         num_of_orders[num.name] += 1
    #     else:
    #         num_of_orders[num.name] == 1

    specific_food = Food.objects.get(name__icontains='Jollof Normal')
    orders = specific_food.order_set.all()

    context = {'foods':all_foods, 'orders':orders}
    return render(request, 'foods.html', context)