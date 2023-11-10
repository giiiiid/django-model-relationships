from django.urls import path
from . import views

urlpatterns=[
    path('orders', views.orders, name='orders'),
    path('customers/<str:name>', views.customers, name='customers'),
    path('foods', views.foods, name='foods'), 
    path('create_order/<str:name>', views.create_order, name='create_order'),
    path('api', views.api, name='api')
]