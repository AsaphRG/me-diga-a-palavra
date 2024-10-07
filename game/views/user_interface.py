from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from databases.forms import ThemeChoiceForm
from databases.models import Word, Theme, Game
from django.contrib.messages import error, info, warning, success

def games(request:HttpRequest):
    games = Game.objects.filter(owner=request.user)

    context = {
        'games': games
    }
    return render(request, 'user/games.html', context=context)