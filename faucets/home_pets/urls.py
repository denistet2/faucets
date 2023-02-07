from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('news/', News.as_view(), name='news'),
    path('volunteering/', volunteering, name='volunteering'),
    path('transportation/', transportation, name='transportation'),
    path('benefit/', benefit, name='benefit'),
    path('wards/', PetsHome.as_view(), name='wards'),
    path('tohome/', tohome, name='tohome'),
    path('temporarily/', temporarily, name='temporarily'),
    path('transportation_order/', transportation_order, name='transportation_order'),
    path('volunteering_help/', volunteering_help, name='volunteering_help'),
    path('financial_support/', financial_support, name='financial_support'),
    path('food_medicines/', food_medicines, name='food_medicines'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', registrations, name='register'),
]

