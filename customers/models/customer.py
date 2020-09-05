from django.db import models
from .category import Category


class Customer(models.Model):
    first_name = models.CharField(max_length=60, default='')
    last_name = models.CharField(max_length=60, default='')
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField(unique=True, default='')
    password = models.CharField(max_length=500)
    image = models.ImageField(upload_to='customers/images', default='')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='date_registered', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    @staticmethod
    def get_customer_by_email(email):
        return Customer.objects.get(email=email)
