from django.contrib import admin

from .models import Customer, Product, Order, Tag


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email')
    list_display_links = ('id', 'first_name', 'last_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'date_created')
    list_display_links = ('id', 'name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'status', 'date_created')
    list_display_links = ('id', 'customer', 'product')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created')
    list_display_links = ('id', 'name')
