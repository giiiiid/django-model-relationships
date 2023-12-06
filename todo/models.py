from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created']
