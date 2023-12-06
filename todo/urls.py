from django.urls import path
from .views import TodoAPI, TodoDetail #ListTodo, create_todo, list_todo #CreateTodo

urlpatterns = [
    path('todo', TodoAPI.as_view(), name='todo'),
    path('tdetail/<str:name>', TodoDetail.as_view(), name='tdetail'),
    # path('createtodo', create_todo, name='createtodo'),
    # path('list', ListTodo.as_view(), name='list'), 
    # path('listtodo', list_todo, name='listtodo')
]