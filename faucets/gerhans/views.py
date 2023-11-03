from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import *
from .forms import *
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, 'gerhans/index.html')


def about(request):
    return render(request, 'gerhans/about.html')


def contacts(request):
    return render(request, 'gerhans/contacts.html')


def news(request):
    return render(request, 'gerhans/news.html')


def volunteering(request):
    return render(request, 'gerhans/volunteering.html')


def transportation(request):
    return render(request, 'gerhans/transportation.html')


def categories(request):
    return render(request, 'gerhans/categories.html')


#def faucets(request):
#
#    pets = HomePet.objects.all()
#    return render(request, 'gerhans/faucets.html',{'pets': pets})
class faucets(ListView):
    paginate_by = 3
    model = faucets
    template_name = 'gerhans/faucets.html'
    context_object_name = 'items'
    extra_context = {'title':'Смесители'}

def basin(request):

    item = items.objects.all()
    paginator = Paginator(item,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gerhans/basin.html',{'page_obj': page_obj ,'item': items})

def accessories(request):

    pets = items.objects.all()
    return render(request, 'gerhans/accessories.html',{'item': items})

def garden(request):

    pets = items.objects.all()
    return render(request, 'gerhans/garden.html',{'item': items})

def sewerage(request):

    pets = items.objects.all()
    return render(request, 'gerhans/sewerage.html',{'item': items})

def favorites(request):

    pets = Item.objects.all()
    return render(request, 'gerhans/favorites.html',{'item': items})


def tohome(request):
    if request.method == "POST":
        form = AdToHomeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdToHomeForm()

    return render(request, 'gerhans/tohome.html',{'form': form})


def temporarily(request):
    if request.method == 'POST':
        form = AdOrderItemTemporarytyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdOrderItemTemporarytyForm()

    return render(request, 'gerhans/temporarily.html',{'form': form})


def transportation_order(request):
    if request.method == 'POST':
        form = AdTransportHelpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdTransportHelpForm()

    return render(request, 'gerhans/transportation_order.html',{'form': form})



def volunteering_help(request):
    if request.method == 'POST':
        form = AdVolOrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdVolOrderForm()
    return render(request, 'gerhans/volunteering_help.html',{'form': form})


def financial_support(request):
    return render(request, 'gerhans/financial_support.html')


def food_medicines(request):
    return render(request, 'gerhans/food_medicines.html')


def food_medicines_help(request):
    if request.method == 'POST':
        form = AdFoodMedicinesHelpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdFoodMedicinesHelpForm()
    return render(request, 'gerhans/food_medicines_help.html',{'form': form})

