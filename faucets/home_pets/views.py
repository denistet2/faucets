from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import *
from .forms import *

# Create your views here.


def index(request):
    return render(request, 'home_pets/index.html')


def about(request):
    return render(request, 'home_pets/about.html')


def contacts(request):
    return render(request, 'home_pets/contacts.html')


def news(request):
    return render(request, 'home_pets/news.html')


def volunteering(request):
    return render(request, 'home_pets/volunteering.html')


def transportation(request):
    return render(request, 'home_pets/transportation.html')


def benefit(request):
    return render(request, 'home_pets/benefit.html')


def wards(request):
    pets = HomePet.objects.all()
    return render(request, 'home_pets/wards.html',{'pets': pets})


def tohome(request):
    if request.method == "POST":
        form = AdToHomeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdToHomeForm()

    return render(request, 'home_pets/tohome.html',{'form': form})


def temporarily(request):
    if request.method == 'POST':
        form = AdOrderPetTemporarytyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdOrderPetTemporarytyForm()

    return render(request, 'home_pets/temporarily.html',{'form': form})


def transportation_order(request):
    if request.method == 'POST':
        form = AdTransportHelpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdTransportHelpForm()

    return render(request, 'home_pets/transportation_order.html',{'form': form})



def volunteering_help(request):
    if request.method == 'POST':
        form = AdVolOrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdVolOrderForm()
    return render(request, 'home_pets/volunteering_help.html',{'form': form})


def financial_support(request):
    return render(request, 'home_pets/financial_support.html')


def food_medicines(request):
    return render(request, 'home_pets/food_medicines.html')

