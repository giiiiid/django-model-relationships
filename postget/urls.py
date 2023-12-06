from django.urls import path, include
from . import views
# from api import views
# from api import urls

urlpatterns=[
    path('orders', views.orders, name='orders'),
    path('customers/<str:name>', views.customers, name='customers'),
    path('foods', views.foods, name='foods'), 
    path('create_order/<str:name>', views.create_order, name='create_order'),
    path('api/', include('postget.api.urls'))
]