from django.urls import path
from . import views

urlpatterns = [
    path('fashion', views.fashion, name='fashion'),
    path('mobiles', views.mobiles, name='mobiles'),
    path('electronics', views.electronics, name='electronics'),
    path('books', views.books, name='books'),
]
