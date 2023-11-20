from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('news/', news, name='news'),
    path('categories/', categories, name='categories'),
    path('faucets/', ProductList.as_view(), name='faucets'),
    path('basins/', ProductList.as_view(), name='basins'),
    path('accessories/', ProductList.as_view(), name='accessories'),
    path('favorites/', FavoritesList, name='favorites'),
    path('sewerage/', ProductList.as_view(), name='sewerage'),
    path('garden/', ProductList.as_view(), name='garden'),
    path('financial_support/', financial_support, name='financial_support'),
    path('basket/', basket, name='basket'),    # path('temporarily/', temporarily, name='temporarily'),
    path('delivery/', delivery, name='delivery'),    # path('volunteering_help/', volunteering_help, name='volunteering_help'),
    path('parts/', parts, name='parts'),    # path('food_medicines_help/', food_medicines_help, name='food_medicines_help'),
    path('gift/', gift, name='gift'),
]
