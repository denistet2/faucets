from django.contrib import admin
from .models import *

class HomePetAdmin(admin.ModelAdmin):
    list_display = ('pets','foto','name_pets','age_pets','text_about_pets')
admin.site.register(HomePet,HomePetAdmin)
class OrderPetAdmin(admin.ModelAdmin):
    list_display = ('name','phone','pets','message','order_data')
admin.site.register(OrderPet,OrderPetAdmin)

class OrderPetTemporarityAdmin(admin.ModelAdmin):
    list_display = ('name','phone','pets','order_data','start_time','end_time','message')
admin.site.register(OrderPetTemporarity,OrderPetTemporarityAdmin)


class TransportationOrderAdmin(admin.ModelAdmin):
    list_display = ('driver_name','phone','transport_type','order_data','start_point','end_point','message')
admin.site.register(TransportationOrder,TransportationOrderAdmin)


class VolOrderAdmin(admin.ModelAdmin):
    list_display = ('name_vol','phone','vol_type','data_order','start_time','end_time','message')
admin.site.register(VolOrder,VolOrderAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('foto','text_news','data')
admin.site.register(News, NewsAdmin)

class MedicamentosAddAdmin(admin.ModelAdmin):
    list_display = ('med_type','med_weight','name','phone')
admin.site.register(MedicamentosAdd, MedicamentosAddAdmin)


class ForageAddAdmin(admin.ModelAdmin):
    list_display = ('forage_type','forage_weight','name','phone')
admin.site.register(ForageAdd, ForageAddAdmin)
admin.site.register(ItemAdd)
# admin.site.register(Stock)
