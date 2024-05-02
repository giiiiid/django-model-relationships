from .serializers import OrderSerializer
from ..models import Order
from rest_framework import response, status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.core.paginator import Paginator

class OrderAPI(APIView):
    serializer_class = OrderSerializer

    def get(self, request):
        queryset = Order.objects.all()
        
        page_num = request.GET.get('page', 1)
        paginator = Paginator(queryset,2)
        print(paginator.per_page)
        serializer = self.serializer_class(paginator.page(page_num), many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# errors because I am not using a user
# class UpdateOrderAPI(RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderSerializer
#     lookup_field = ["id"]

#     def get_queryset(self):
#         queryset = Order.objects.filter("?")
#         return queryset