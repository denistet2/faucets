from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('news/', news, name='news'),
    path('volunteering/', volunteering, name='volunteering'),
    path('transportation/', transportation, name='transportation'),
    path('categories/', categories, name='categories'),
    path('faucets/', faucets.as_view(), name='faucets'),
    path('basin/', basin, name='basin'),
    path('accessories/', accessories, name='accessories'),
    path('favorites/', favorites, name='favorites'),
    path('sewerage/', sewerage, name='sewerage'),
    path('garden/', garden, name='garden'),
    path('tohome/', tohome, name='tohome'),
    path('temporarily/', temporarily, name='temporarily'),
    path('transportation_order/', transportation_order, name='transportation_order'),
    path('volunteering_help/', volunteering_help, name='volunteering_help'),
    path('financial_support/', financial_support, name='financial_support'),
    path('food_medicines/', food_medicines, name='food_medicines'),
    path('food_medicines_help/', food_medicines_help, name='food_medicines_help'),
]
