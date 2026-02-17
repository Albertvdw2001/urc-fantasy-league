from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.teams.models import Team

# Create your models here.

class User(AbstractUser):
    is_fantasy_user = models.BooleanField(default=False) 
    has_picked_fav_team = models.BooleanField(default=False)
    favourite_team = models.OneToOneField(Team, null=True, blank=True, on_delete=models.SET_DEFAULT)

    def has_necessary_fantasy_fields(self) -> bool:
        conditions = [
            hasattr(self, 'fantasy_team'),
            self.has_picked_fav_team
        ]
        return

    def enable_fantasy_access(self):
        if has_necessary_fantasy_fields(self):
            self.is_fantasy_user = True
            self.save()
            return