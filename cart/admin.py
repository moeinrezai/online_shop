from django.contrib import admin
from . import models
from .models import DiscountCode


# Register your models here.

class Order_ItemAdmin(admin.TabularInline):
    model = models.Order_Item



@admin.register(models.Order)
class Order_Admin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')
    inlines = (Order_ItemAdmin,)
    list_filter = ('is_paid',)


@admin.register(models.DiscountCode)
class DiscountCode_Admin(admin.ModelAdmin):
    list_display = ('name', 'discount', "quantity")

