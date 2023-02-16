from django.urls import path, include
from django.contrib import admin

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('news/', News.as_view(), name='news'),
    path('volunteering/', volunteering, name='volunteering'),
    path('transportation/', transportation, name='transportation'),
    path('benefit/', benefit, name='benefit'),
    path('wards/', PetsHome.as_view(), name='wards'),
    path('to_home/', tohome, name='to_home'),
    path('temporarily/', temporarily, name='temporarily'),
    path('transportation_order/', transportation_order, name='transportation_order'),
    path('volunteering_help/', volunteering_help, name='volunteering_help'),
    path('financial_support/', financial_support, name='financial_support'),
    path('food_medicines/', food_medicines, name='food_medicines'),
    path('food_medicines_help/', food_medicines_help, name='food_medicines_help'),

]

