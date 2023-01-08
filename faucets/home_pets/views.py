from django.shortcuts import render
from .models import HomePet

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
    return render(request, 'home_pets/tohome.html')


def temporarily(request):
    return render(request, 'home_pets/temporarily.html')

def transportation_order(request):
    return render(request, 'home_pets/transportation_order.html')



def volunteering_help(request):
    return render(request, 'home_pets/volunteering_help.html')


def financial_support(request):
    return render(request, 'home_pets/financial_support.html')


def food_medicines(request):
    return render(request, 'home_pets/food_medicines.html')

