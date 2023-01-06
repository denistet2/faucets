from django.contrib import admin

# Register your models here.

from .models import home_pet
admin.site.register(home_pet)

from .models import help_list
admin.site.register(help_list)

from .models import order_help
admin.site.register(order_help)

from .models import order_pet
admin.site.register(order_pet)
