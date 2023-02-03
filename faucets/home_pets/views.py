from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DataMixin
from django.views.generic import ListView
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request, 'home_pets/index.html')


def about(request):
    return render(request, 'home_pets/about.html')


def contacts(request):
    return render(request, 'home_pets/contacts.html')


class News(ListView):
    paginate_by = 3
    model = News
    template_name = 'home_pets/news.html'
    context_object_name = 'add_news'
    # return render(request, 'home_pets/news.html')


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
    extra_context = {'title':'Подопечные'}

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


class UserCreatingForm:
    pass


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'home_pets/registrations.html'
    # success_url = revers_lazy('login')

    def get_context_data(self,object_list=None, **kwargs):
        context = super().get_context_data()
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()+list(c_def.items)))