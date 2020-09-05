from django.contrib import admin
from .models import Product
from .models import Category


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'image']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
