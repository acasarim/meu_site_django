from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
#from django.urls import path

def home(request):
    return render(request, 'recipes/pages/Home.html', context={
        'nome': 'Alexandre Casarin',
    })
