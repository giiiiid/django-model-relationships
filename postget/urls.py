from django.urls import path
from . import views

urlpatterns=[
    path('orders', views.orders, name='orders'),
    path('customers/<str:name>', views.customers, name='customers'),
    path('foods', views.foods, name='foods')
]