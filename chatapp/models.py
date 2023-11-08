from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.

class Room(models.Model):
    name_of_room = models.CharField(max_length=100)

    # def get_absolute_urls(self):
    #     return reverse('room', kwargs={'name':self.name_of_room})

class Message(models.Model):
    username = models.CharField(max_length=150)
    message = models.CharField(max_length=1000000)
    date_of_message = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=150)
