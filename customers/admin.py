from django.contrib import admin
from .models.customer import Customer
from .models.category import Category


class AdminCustomer(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone']


# Register your models here.

admin.site.register(Customer, AdminCustomer)
admin.site.register(Category)
