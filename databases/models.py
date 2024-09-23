from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)
    ddi = models.CharField(max_length=255)


class State(models.Model):
    name = models.CharField(max_length=255)
    ddd = models.CharField(max_length=255)


class CustomUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    SEX_CHOICES = [
        (MALE, 'Masculino'),
        (FEMALE, 'Feminino'),
        (OTHER, 'Outro'),
    ]

    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True, verbose_name='Sexo')
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='País')
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Estado')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')


# class Visit(models.Model):
#     page = models.CharField(blank=False, null=False)
#     # user = 
#     dt_access = models.DateTimeField(default=timezone.now())

