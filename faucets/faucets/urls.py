from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_pets.urls')),
    path('about/', include('home_pets.urls')),
    path('contacts/', include('home_pets.urls')),
    path('news/', include('home_pets.urls')),
    path('volunteering/', include('home_pets.urls')),
    path('transportation/', include('home_pets.urls')),
    path('benefit/', include('home_pets.urls')),
    path('wards/', include('home_pets.urls')),
    path('tohome/', include('home_pets.urls')),
    path('temporarily/', include('home_pets.urls')),
    path('transportation_order/', include('home_pets.urls')),
    path('volunteering_help/', include('home_pets.urls')),
    path('financial_support/', include('home_pets.urls')),
    path('food_medicines/', include('home_pets.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
