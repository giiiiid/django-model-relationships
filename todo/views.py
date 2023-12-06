from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status
# Create your views here.

class CreateTodo(CreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    #     return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListTodo(ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Todo.objects.filter(owner=self.request.user)
        return queryset

