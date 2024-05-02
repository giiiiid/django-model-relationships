from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status, decorators
from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.core.paginator import Paginator
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

# class TodoAPI(APIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]

#     filterset_fields = ["name", "desc", "is_complete"]

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data, status=status.HTTP_201_CREATED)
#         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # @decorators.api_view(["GET"])
#     def get(self, request):
#         queryset = Todo.objects.all()

#         page_num = request.GET.get('page',1)
#         paginator = Paginator(queryset,2)
        
#         serializer = self.serializer_class(paginator.page(page_num), many=True)
#         return response.Response(serializer.data)
    
    

# class TodoDetail(RetrieveUpdateDestroyAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'

#     def get_queryset(self, *args, **kwargs):
#         queryset = Todo.objects.filter(owner=self.request.user)
#         return queryset


# @decorators.api_view(["GET"])
# def search_list(request):
#     queryset = Todo.objects.all()
#     if request.GET.get('search'):
#         search = request.GET.get('search')
#         queryset = Todo.objects.filter(Q(name__icontains=search) | Q(desc__icontains=search))
#     serializer = TodoSerializer(queryset, many=True)
#     filter_backends = (SearchFilter)
#     search_fields = ("name", "desc")
#     return response.Response(serializer.data)
    
