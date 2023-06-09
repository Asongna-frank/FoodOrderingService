from django.contrib import admin
from .models import Admin, Menu, Foodbuyer, Foodvendor, Image, Dishes, Shoppingcart, Orderfood

# Register your models here.
admin.site.register(Admin)
admin.site.register(Menu)
admin.site.register(Foodbuyer)
admin.site.register(Foodvendor)
admin.site.register(Image)
admin.site.register(Dishes)
admin.site.register(Shoppingcart)
admin.site.register(Orderfood)
