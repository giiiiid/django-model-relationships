from django.urls import path
from .views import OrderAPI

urlpatterns = [
    path('order', OrderAPI.as_view(), name="order_api")
]