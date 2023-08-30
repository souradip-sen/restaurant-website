from django.contrib import admin

# Register your models here.
from .models import Menu, MenuCategory, Booking
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Booking)
