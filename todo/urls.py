from django.urls import path
from .views import CreateTodo, ListTodo

urlpatterns = [
    path('create', CreateTodo.as_view(), name='create'),
    path('list', ListTodo.as_view(), name='list')
]