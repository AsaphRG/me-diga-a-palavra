from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from databases.forms import ThemeChoiceForm
from databases.models import Word, Theme, Game, Move
from django.contrib.messages import error, info, warning, success
from game.game_logic.check_letter import reveal_letters
from datetime import datetime
import random


# Create your views here.
@login_required(login_url='forca:login')
def game(request: HttpRequest, id):
    game = get_object_or_404(Game, owner=request.user, id=id)
    print(reveal_letters('e', game.secret_word, game.discovered_word))
    print(reveal_letters('b', game.secret_word, game.discovered_word))
    print(reveal_letters('g', game.secret_word, game.discovered_word))
    if game.finished:
        info(request, f'Partida finalizada em {game.finished_at.strftime("%d/%m/%Y")}')
        return redirect('forca:games')
    
    moves = Move.objects.filter(game=game.id)
    wrong_answers = []
    [wrong_answers.append(guess.letter) for guess in moves if not guess.right]

    if request.method == 'POST':
        guess = request.POST.get('guess')

        if guess not in moves:
            if guess.casefold() in game.secret_word.casefold():
                Move.objects.create(letter=guess, game=game, right=True)
                game.discovered_word = reveal_letters(guess, game.secret_word, game.discovered_word)
                game.save()
            else:
                Move.objects.create(letter=guess, game=game)
                wrong_answers.append(guess)
                if len(wrong_answers) > 4:
                    game.finished = True
                    game.finished_at = datetime.now()
                    game.save()
                    return redirect('forca:game_over')

    context = {
        'image': '/static/game/images/1.png',
        'forca': '/static/game/images/forca.png',
        'game_id': game.id,
        'theme': game.theme,
        'discovered_word': game.discovered_word,
        'wrong_answers': wrong_answers,
    }
    return render(request, 'game/game.html', context=context)


@login_required(login_url='forca:login')
def createGame(request: HttpRequest):
    if request.POST.getlist('themesList[]'):
        themes = [int(themestr) for themestr in request.POST.getlist('themesList[]')]
        words = Word.objects.filter(theme__id__in=themes)
        secret_word = random.choice(words)
        discovered_word = '_' * len(secret_word.word)
        game = Game.objects.create(secret_word=secret_word.word, theme=secret_word.theme, discovered_word=discovered_word, owner=request.user)
        reveal_letters(' ', game.secret_word, game.discovered_word)
        return redirect('forca:game', game_id=game.id)
    else:
        warning(request, 'Escolha ao menos um tema')
    return redirect('forca:theme')


@login_required(login_url='forca:login')
def theme(request: HttpRequest):
    themes = Theme.objects.all()
    context = {
        'themes': themes,
    }

    
    return render(request, 'game/themeChoice.html', context=context)


@login_required(login_url='forca:login')
def game_over(request: HttpRequest):
    return render(request, 'game/game_over.html')