from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpRequest

from django.urls import reverse

from databases import forms


def login(request: HttpRequest):
    context = {
        'form_action': reverse('forca:login'),
        'form': AuthenticationForm(request)
    }

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('forca:home')
        messages.error(request, f'Login inválido.')
    
    return render(request, 'authentication/login.html', context=context)


def register(request: HttpRequest):
    context = {
        'form_action': reverse('forca:register'),
        'form': forms.CustomUserCreationForm(),
    }

    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            authenticated_user = auth.authenticate(username=user.username, password=form.cleaned_data.get('password1'))
            if authenticated_user is not None:
                auth.login(request, authenticated_user)
                messages.info(request, f'Bem vindo, {user.first_name}!')
                return redirect('forca:home')

    return render(request, 'authentication/register.html', context=context)


@login_required(login_url='forca:login')
def modify(request: HttpRequest):
    context={
        'form_action': reverse('forca:modify'),
        'form': forms.ModifyUserForm(instance=request.user)
    }

    if request.method == 'POST':
        form = forms.ModifyUserForm(data=request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            context['form'] = form

    return render(request, 'authentication/modify.html', context=context)


@login_required(login_url='forca:login')
def logout(request: HttpRequest):
    auth.logout(request)
    return redirect('forca:login')