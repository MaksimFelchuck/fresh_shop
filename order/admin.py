from django.contrib import admin

# Register your models here.
from order.models import *


@admin.register(Order, ProductInOrder)
class PersonAdmin(admin.ModelAdmin):
    pass
