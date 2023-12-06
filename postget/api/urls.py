from django.urls import path
from .views import OrderAPI

urlpatterns = [
    path('createapi/', OrderAPI.as_view(), name="order_api")
]