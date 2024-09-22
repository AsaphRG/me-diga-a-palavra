from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

# Create your views here.
@login_required(login_url='forca:login')
def home(request: HttpRequest):
    context = {}
    return render(request, 'game/home.html', context=context)


def login(request: HttpRequest):
    context = {}
    return render(request, 'game/login.html', context=context)

def register(request: HttpRequest):
    context = {}
    return render(request, 'game/register.html', context=context)
