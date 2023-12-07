from rest_framework import serializers
from ..models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id" ,"location", "invoice", "delivery", "customer_name"]