from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_fantasy_user = models.BooleanField(default=False) 

    def enable_fantasy_access(self):
        self.is_fantasy_user = True
        self.save()