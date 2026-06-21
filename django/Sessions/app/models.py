from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    password_verification = models.CharField(max_length=64, null=True)
    
    class Meta:
        db_table = "Form"

class Tip(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    contenu = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Tip"