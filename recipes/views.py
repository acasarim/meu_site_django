from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path

def home(request):
    return render(request, 'recipes/Home.html')

def contato(request):
    return HttpResponse('Contato')

def sobre(request):
    return HttpResponse('Sobre')
