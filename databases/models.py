from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)
    ddi = models.CharField(max_length=255)


class State(models.Model):
    name = models.CharField(max_length=255)
    ddd = models.CharField(max_length=255)


class CustomUser(AbstractUser):
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.DO_NOTHING)
    birth_date = models.DateField(blank=True, null=True)


# class Visit(models.Model):
#     page = models.CharField(blank=False, null=False)
#     # user = 
#     dt_access = models.DateTimeField(default=timezone.now())

