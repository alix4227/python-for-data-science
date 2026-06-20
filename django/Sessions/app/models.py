from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    password_verification = models.CharField(max_length=64, null=True)
    
    class Meta:
        db_table = "Form"