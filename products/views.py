from django.shortcuts import render
from .models import Product


# Create your views here.

def fashion(request):
    products = Product.get_all_products()
    return render(request, 'products/fashion/fashion.html', {'products_mobiles': products})


def books(request):
    products = Product.get_all_products()
    return render(request, 'products/books/books.html', {'products_mobiles': products})


def electronics(request):
    products = Product.get_all_products()
    return render(request, 'products/electronics/electronics.html', {'products_mobiles': products})


def mobiles(request):
    products = Product.get_all_products()
    return render(request, 'products/mobiles/mobiles.html', {'products_mobiles': products})
