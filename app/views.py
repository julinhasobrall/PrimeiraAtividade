from django.shortcuts import render
from django.http import HttpResponse  # adiciona isso

def mensagem(request):
    return  render(request, 'mensagem.html')