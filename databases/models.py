from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from encrypted_model_fields.fields import EncryptedCharField


# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=255, verbose_name='Nome do País')
    ddi = models.CharField(max_length=255, verbose_name='DDI')

    class Meta:    
        verbose_name = 'País'
        verbose_name_plural = 'Países'


class State(models.Model):
    state_name = models.CharField(max_length=255, verbose_name='Nome do estado')
    ddd = models.CharField(max_length=255, verbose_name='DDD')
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


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


class Theme(models.Model):
    theme_name = models.CharField(max_length=255, verbose_name='Tema')

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self) -> str:
        return self.theme_name


class Word(models.Model):
    word = models.CharField(max_length=255, verbose_name='Palavra')
    theme = models.ForeignKey(Theme, on_delete=models.DO_NOTHING, verbose_name='Tema')
    
    class Meta:
        verbose_name = 'Palavra'
        verbose_name_plural = 'Palavras'
    
    def __str__(self) -> str:
        return self.word


class Game(models.Model):
    secret_word = EncryptedCharField(max_length=255, verbose_name='Palavra secreta')
    theme = models.ForeignKey(Theme, on_delete=models.DO_NOTHING, verbose_name='Tema')
    discovered_word = models.CharField(max_length=255, verbose_name='Palavra descoberta')
    finished = models.BooleanField(verbose_name='Finalizado', default=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name='Jogador')
    started_at = models.DateTimeField(default=timezone.now, verbose_name='Início')
    finished_at = models.DateTimeField(null=True, blank=True, verbose_name='Fim')
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

    def __str__(self) -> str:
        return super().__str__()


class Move(models.Model):
    letter = models.CharField(max_length=1, verbose_name='Letra')
    right = models.BooleanField(verbose_name="Certo", default=False)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, verbose_name='Jogo')
    time = models.DateTimeField(default=timezone.now, verbose_name='Hora da jogada')
    
    class Meta:
        verbose_name = 'Jogada'
        verbose_name_plural = 'Jogadas'
