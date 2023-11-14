from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('news/', news, name='news'),
    path('categories/', categories, name='categories'),
    path('faucets/', FaucetsList.as_view(), name='faucets'),
    path('basins/', BasinsList.as_view(), name='basins'),
    path('accessories/', AccessoriesList.as_view(), name='accessories'),
    path('favorites/', FavoritesList, name='favorites'),
    path('sewerage/', SewerageList.as_view(), name='sewerage'),
    path('garden/', GardenItemList.as_view(), name='garden'),
    path('financial_support/', financial_support, name='financial_support'),
    path('basket/', basket, name='basket'),    # path('temporarily/', temporarily, name='temporarily'),
    path('delivery/', delivery, name='delivery'),    # path('volunteering_help/', volunteering_help, name='volunteering_help'),
    path('parts/', parts, name='parts'),    # path('food_medicines_help/', food_medicines_help, name='food_medicines_help'),
    path('gift/', gift, name='gift'),
]
