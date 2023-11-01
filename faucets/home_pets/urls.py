from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('news/', news, name='news'),
    path('volunteering/', volunteering, name='volunteering'),
    path('transportation/', transportation, name='transportation'),
    path('categories/', categories, name='categories'),
    path('faucets/', faucets, name='faucets'),
    path('basin/', basin, name='basin'),
    path('favorites/', favorites, name='favorites'),
    path('tohome/', tohome, name='tohome'),
    path('temporarily/', temporarily, name='temporarily'),
    path('transportation_order/', transportation_order, name='transportation_order'),
    path('volunteering_help/', volunteering_help, name='volunteering_help'),
    path('financial_support/', financial_support, name='financial_support'),
    path('food_medicines/', food_medicines, name='food_medicines'),
    path('food_medicines_help/', food_medicines_help, name='food_medicines_help'),
]
