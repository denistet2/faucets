from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Страница домашних питомцев")

def news(request):
    return HttpResponse("Новости")

def categories(request):
    return HttpResponse("Помощь")