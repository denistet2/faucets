from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic.edit import  CreateView
from django.views.generic import ListView
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
    news_list = News.objects.all()
    paginator = Paginator(news_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home_pets/news.html',{ 'page_obj' : page_obj})


def volunteering(request):
    return render(request, 'home_pets/volunteering.html')


def transportation(request):
    return render(request, 'home_pets/transportation.html')


def benefit(request):
    return render(request, 'home_pets/benefit.html')

class PetsHome(ListView):
    paginate_by = 3
    model = HomePet
    template_name = 'home_pets/wards.html'
    context_object_name = 'pets'

# def wards(request):
#
#     pets = HomePet.objects.all()
#     return render(request, 'home_pets/wards.html',{'pets': pets})


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


def food_medicines_help(request):
    if request.method == 'POST':
        form = AdFoodMedicinesHelpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdFoodMedicinesHelpForm()
    return render(request, 'home_pets/food_medicines_help.html',{'form': form})




class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'faucet/register.html'
    success_url = revers_lazy('login')

    def get_context_data(self, object_list = None, **kwargs):
        contex = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    # https: // www.youtube.com / watch?v = QK4qbVyY7oU & list = PLA0M1Bcd0w8xO_39zZll2u1lz_Q - Mwn1F & index = 19