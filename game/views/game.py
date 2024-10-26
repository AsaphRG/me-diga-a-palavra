from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from databases.forms import ThemeChoiceForm
from databases.models import Word, Theme, Game, Move
from django.contrib.messages import error, info, warning, success
from game.game_logic.check_letter import reveal_letters
from django.utils import timezone
import random


# Create your views here.
@login_required(login_url='forca:login')
def game(request: HttpRequest, id):
    css_class = ['first-image', 'second-image', 'third-image', 'fourth-image', 'fiveth-image']
    game = get_object_or_404(Game, owner=request.user, id=id)
    
    if game.finished:
        return redirect('forca:game_finished', game.id)

    if request.POST.get('random_number'):
        random_number = request.POST.get('random_number')
    else:
        random_number = random.randint(1, 5)
    
    moves = Move.objects.filter(game=game.id)
    moves_list = [move.letter for move in moves]
    wrong_answers = []
    [wrong_answers.append(guess.letter) for guess in moves if not guess.right]

    if request.method == 'POST':
        guess = request.POST.get('guess')

        if guess not in moves_list:
            if guess.casefold() in game.secret_word.casefold():
                Move.objects.create(letter=guess, game=game, right=True)
                game.discovered_word = reveal_letters(guess, game.secret_word, game.discovered_word)
                if "_" not in game.discovered_word:
                    game.finished = True
                    game.win = True
                    game.finished_at = timezone.now()
                    game.save()
                    return redirect('forca:win')
                game.save()
            else:
                if guess not in wrong_answers:
                    Move.objects.create(letter=guess, game=game)
                    wrong_answers.append(guess)
                    random_number = random.randint(1, 5)
                if len(wrong_answers) > 4:
                    game.finished = True
                    game.finished_at = timezone.now()
                    game.save()
                    return redirect('forca:game_over')
    

    context = {
        'random_number': random_number,
        'forca': '/static/game/images/forca.png',
        'game_id': game.id,
        'theme': game.theme,
        'discovered_word': game.discovered_word,
        'wrong_answers': wrong_answers,
        'class': css_class[len(wrong_answers)]
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
        game.discovered_word = reveal_letters(' ', game.secret_word, game.discovered_word)
        game.discovered_word = reveal_letters("'", game.secret_word, game.discovered_word)
        game.discovered_word = reveal_letters("-", game.secret_word, game.discovered_word)
        game.save()
        return redirect('forca:game', id=game.id)
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


@login_required(login_url='forca:login')
def win(request: HttpRequest):
    return render(request, 'game/win.html')
