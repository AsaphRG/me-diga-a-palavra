from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from databases.models import *


# Create your views here.
@login_required(login_url='forca:login')
def load_all(request: HttpRequest):
    temas = ('Animal', 'Móvel', 'País', 'Cor')
    listaPalavras = []

    for tema in temas:
        tema_palavra = Theme.objects.filter(theme_name=tema)[0]
        with open('C:\\Users\\asaph\\Downloads\\'+tema+'.txt', 'r', encoding='UTF-8') as file:
            texto = file.read()
            palavras = texto.split("; ")
            for palavra in palavras:
                listaPalavras.append((palavra.capitalize().strip(), tema_palavra))
    print(listaPalavras)

    for palavra in listaPalavras:
        Word.objects.create(word=palavra[0], theme=palavra[1])

    context = {}
    return redirect('forca:home')
