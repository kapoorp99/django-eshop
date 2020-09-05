from django.urls import path
from .views import LoginCustomer, logout_customer, SignupCustomer

urlpatterns = [
    path('login', LoginCustomer.as_view(), name='login'),
    path('logout', logout_customer, name='logout'),
    path('signup', SignupCustomer.as_view(), name='signup'),
]
