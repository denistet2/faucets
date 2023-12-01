from django.urls import path
from .views import *
app_name = 'gerhans'

urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', GSLoginView.as_view(), name='login'),
    path('accounts/logout/', GSLogoutView.as_view(), name='logout'),
    # path('contacts/', contacts, name='contacts'),
    # path('news/', news, name='news'),
    # path('categories/', categories, name='categories'),
    # path('faucets/', ProductList.as_view(), name='faucets'),
    # path('basins/', ProductList.as_view(), name='basins'),
    # path('accessories/', ProductList.as_view(), name='accessories'),
    # path('favorites/', FavoritesList, name='favorites'),
    # path('sewerage/', ProductList.as_view(), name='sewerage'),
    # path('garden/', ProductList.as_view(), name='garden'),
    # path('financial_support/', financial_support, name='financial_support'),
    # path('basket/', basket, name='basket'),    # path('temporarily/', temporarily, name='temporarily'),
    # path('delivery/', delivery, name='delivery'),    # path('volunteering_help/', volunteering_help, name='volunteering_help'),

]
