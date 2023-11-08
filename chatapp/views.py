from django.shortcuts import render, redirect, reverse
from .models import Room, Message
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')
def room(request,name):
    name_of_room = Room.objects.get(name_of_room=name) 
    user = request.GET.get('username')
    return render(request, 'room.html', {
        'name':name,
        'username':user,
        })

def checkroom(request):
    name_of_room = request.POST['room_name']
    user = request.POST['username']

    if Room.objects.filter(name_of_room=name_of_room).exists():
        return redirect('/chat/room/'+ name_of_room +'?username='+user)
    else:
        new_room = Room.objects.create(name_of_room=name_of_room)
        new_room.save()
        return redirect('/chat/room/'+ name_of_room +'?username='+user)

def send(request):
    message = request.POST.get('message')
    user = request.POST.get('username')
    name_of_room = request.POST.get('room_id')
    new_message = Message.objects.create(username=user,message=message,room=name_of_room)
    new_message.save()
    return HttpResponse('Message sent')
