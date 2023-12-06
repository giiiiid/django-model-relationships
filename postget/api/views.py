from .serializers import OrderSerializer
from ..models import Order
from rest_framework import response, status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class OrderAPI(APIView):
    serializer_class = OrderSerializer

    def get(self, request):
        queryset = Order.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)