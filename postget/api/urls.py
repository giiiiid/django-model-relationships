from django.urls import path
from .views import OrderAPI, UpdateOrderAPI

urlpatterns = [
    path('createapi/', OrderAPI.as_view(), name="order_api"), 
    path('updateapi/<int:id>', UpdateOrderAPI.as_view(), name="update_api")
]