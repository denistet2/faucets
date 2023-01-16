from django.contrib import admin
from .models import HomePet, OrderPet, OrderPetTemporarity, TransportationOrder, VolOrder


admin.site.register(HomePet)
admin.site.register(OrderPet)
admin.site.register(OrderPetTemporarity)
admin.site.register(TransportationOrder)
admin.site.register(VolOrder)
