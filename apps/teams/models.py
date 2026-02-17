from django.db.models import CharField
from django.db import models
from django_countries.fields import CountryField 

# Create your models here.

class Team(models.Model):
    name = models.CharField()
    country = CountryField()