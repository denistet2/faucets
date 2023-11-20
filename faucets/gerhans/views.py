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


def gift(request):
    return render(request, 'gerhans/gift.html')


def delivery(request):
    return render(request, 'gerhans/delivery.html')


def categories(request):
    return render(request, 'gerhans/categories.html')



class ProductList(ListView):
    paginate_by = 6
    model = Product
    template_name = 'gerhans/faucets.html'
    context_object_name = 'productlist'
    extra_context = {'title':'Смесители'}



class BasinsList(ListView):
    paginate_by = 3
    model = Product
    template_name = 'gerhans/basin.html'
    context_object_name = 'basinitem'
    extra_context = {'title':'Мойки'}


class AccessoriesList(ListView):
    paginate_by = 3
    model = Product
    template_name = 'gerhans/accessories.html'
    context_object_name = 'accessory'
    extra_context = {'title':'Аксессуары'}

# def garden(request):
#
#     pets = items.objects.all()
#     return render(request, 'gerhans/garden.html',{'item': items})

class GardenItemList(ListView):
    paginate_by = 3
    model = Product
    template_name = 'gerhans/garden.html'
    context_object_name = 'gardenitem'
    extra_context = {'title':'Садовое оборудование'}

class SewerageList(ListView):
    paginate_by = 3
    model = Product
    template_name = 'gerhans/sewerage.html'
    context_object_name = 'sewerageitem'
    extra_context = {'title':'Садовое оборудование'}

# def sewerage(request):
#
#     pets = items.objects.all()
#     return render(request, 'gerhans/sewerage.html',{'item': items})

# def favorites(request):
#
#     items = items.objects.all()
#     return render(request, 'gerhans/favorites.html',{'item': items})


def basket(request):
    if request.method == "POST":
        form = AdBasketForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdBasketForm()

    return render(request, 'gerhans/basket.html',{'form': form})


def FavoritesList(request):
    if request.method == 'POST':
        form = AdFavoritesList(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdFavoritesList()

    return render(request, 'gerhans/favorites.html',{'form': form})


# def transportation_order(request):
#     if request.method == 'POST':
#         form = AdTransportHelpForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AdTransportHelpForm()
#
#     return render(request, 'gerhans/transportation_order.html',{'form': form})



# def volunteering_help(request):
#     if request.method == 'POST':
#         form = AdVolOrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AdVolOrderForm()
#     return render(request, 'gerhans/volunteering_help.html',{'form': form})


def financial_support(request):
    return render(request, 'gerhans/financial_support.html')


def parts(request):
    return render(request, 'gerhans/parts.html')
#
#
# def food_medicines_help(request):
#     if request.method == 'POST':
#         form = AdFoodMedicinesHelpForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AdFoodMedicinesHelpForm()
#     return render(request, 'gerhans/food_medicines_help.html',{'form': form})
#
