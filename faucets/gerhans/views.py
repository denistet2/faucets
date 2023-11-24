from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Rubric, Product
from .forms import *
from django.core.paginator import Paginator

# Create your views here.
# def categories(request):
#     return render(request, 'gerhans/categories.html')
def by_rubric(request, rubric_id):
    categories = Product.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    curent_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'categories': categories, 'rubrics': rubrics, 'current_rubric': curent_rubric}
    return render(request, 'gerhans/categories.html', context)



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






class ProductList(ListView):
    paginate_by = 3
    model = Product
    template_name = 'gerhans/faucets.html'
    context_object_name = 'production'
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



def financial_support(request):
    return render(request, 'gerhans/financial_support.html')


def parts(request):
    return render(request, 'gerhans/parts.html')
