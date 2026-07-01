from django.db import models
from django.contrib.auth.models import *

class Chatroom(models.Model):
    name = models.CharField(max_length=20)
    members = models.ManyToManyField(
        User,
        related_name='chatrooms',
        blank=True
    )
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Chatroom"

class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user}: {self.content}'

    class Meta:
        db_table = "Message"
