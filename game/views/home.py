from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest


# Create your views here.
@login_required(login_url='forca:login')
def home(request: HttpRequest):
    context = {}
    return render(request, 'game/home.html', context=context)
