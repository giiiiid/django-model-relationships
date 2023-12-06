from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status, decorators
# Create your views here.

# class CreateTodo(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]

#     # def perform_create(self, serializer):
#     #     return serializer.save(owner=self.request.user)
#     #     return response.Response(serializer.data, status=status.HTTP_201_CREATED)
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data, status=status.HTTP_201_CREATED)
#         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @decorators.api_view(["POST"])
# def create_todo(request):
#     serializer = TodoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(owner=request.user)
#         return response.Response(serializer.data, status=status.HTTP_201_CREATED)
#     return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ListTodo(ListAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         queryset = Todo.objects.filter(owner=self.request.user)
#         return queryset

# @decorators.api_view(["GET"])
# def list_todo(request):
#     queryset_owner = Todo.objects.filter(owner=request.user)
#     serializer = TodoSerializer(queryset_owner, many=True)
#     return response.Response(serializer.data, status=status.HTTP_200_OK)

class TodoAPI(APIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # @decorators.api_view(["GET"])
    def get(self, request):
        queryset = Todo.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data)

class TodoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "name"

    def get_queryset(self):
        queryset = Todo.objects.filter(owner=self.request.user)
        return queryset