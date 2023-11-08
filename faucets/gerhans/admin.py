from django.contrib import admin
from .models import *


class FaucetsAdmin(admin.ModelAdmin):
    list_display = ('faucets_type', 'foto', 'article', 'price', 'text_about_item', 'published')


admin.site.register(Faucets, FaucetsAdmin)


class BasinsAdmin(admin.ModelAdmin):
    list_display = ('basins_type', 'foto', 'article', 'price', 'text_about_item', 'published')


admin.site.register(Basins, BasinsAdmin)


class AccessoriesListAdmin(admin.ModelAdmin):
    list_display = ('items_type', 'foto', 'article', 'price', 'text_about_item', 'published')


admin.site.register(Accessories, AccessoriesListAdmin)




# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone', 'article', 'message', 'order_data')
#
#
# admin.site.register(OrderItem, OrderItemAdmin)

#
# class OrderItemTemporarityAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone', 'article', 'order_data', 'start_time', 'end_time', 'message')
#
#
# admin.site.register(OrderItemTemporarity, OrderItemTemporarityAdmin)


# class TransportationOrderAdmin(admin.ModelAdmin):
#     list_display = ('driver_name', 'phone', 'transport_type', 'order_data', 'start_point', 'end_point', 'message')
#
#
# admin.site.register(TransportationOrder, TransportationOrderAdmin)
#
#
# class VolOrderAdmin(admin.ModelAdmin):
#     list_display = ('name_vol', 'phone', 'vol_type', 'data_order', 'start_time', 'end_time', 'message')
#
#
# admin.site.register(VolOrder, VolOrderAdmin)
#
#
class MedicamentosAddAdmin(admin.ModelAdmin):
    list_display = ('med_type', 'med_weight', 'name', 'phone')
#
#
# admin.site.register(MedicamentosAdd, MedicamentosAddAdmin)
#
#
# class ForageAddAdmin(admin.ModelAdmin):
#     list_display = ('forage_type', 'forage_weight', 'name', 'phone')
#
#
# admin.site.register(ForageAdd, ForageAddAdmin)
# admin.site.register(ItemAdd)
# # admin.site.register(Stock)
