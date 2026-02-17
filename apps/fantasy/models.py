from django.db import models
from apps.users.models import User
import config.settings as settings

# Create your models here.

class FantasyTeam(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fantasy_team')