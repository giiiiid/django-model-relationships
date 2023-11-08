from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chats.html')