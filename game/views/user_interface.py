from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from databases.forms import ThemeChoiceForm
from databases.models import Word, Theme, Game, Move
from django.contrib.messages import error, info, warning, success
from datetime import timedelta
from django.utils import timezone

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    try:
        hours = total_seconds // 3600
    except ZeroDivisionError:
        hours = 0
    
    try:
        minutes = (total_seconds % 3600) // 60
    except ZeroDivisionError:
        minutes = 0
    
    try:
        seconds = total_seconds % 60
    except ZeroDivisionError:
        seconds = 0
    
    return f"{hours}:{minutes}:{seconds}"

def games(request:HttpRequest):
    games = Game.objects.filter(owner=request.user)

    words = set()
    wins = 0
    losses = 0
    moves_made = 0
    differences = []
    for game in games:
        
        if game.win:
            wins += 1
        elif game.finished and not game.win:
            losses += 1

        moves = Move.objects.filter(game=game)
        moves_made += len(moves)
        words.add(game.secret_word)
        start = game.started_at
        end = game.finished_at
        try:
            differences.append(end - start)
        except TypeError:
            differences.append(timezone.now() - start)
    
    total_difference = sum(differences, timedelta())

    time = total_difference / len(differences)
    games_played = games.count()
    seen_words = len(words)

    context = {
        'games': games,
        'wins': wins,
        'losses': losses,
        'played': games_played,
        'moves_made': moves_made,
        'seen_words': seen_words,
        'avg_playtime': format_timedelta(time),
    }
    return render(request, 'user/games.html', context=context)