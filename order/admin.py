from django.contrib import admin
from .models import OrderItem, Order


class OrderItemAdmin(admin.StackedInline):
    extra = 0
    model = OrderItem
    classes = ['collapse']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]
