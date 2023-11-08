from django.urls import path
from . import views

# urls
urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:name>', views.room, name='room'),
    path('checkroom', views.checkroom, name='checkroom'),
    path('send', views.send, name='send')
]