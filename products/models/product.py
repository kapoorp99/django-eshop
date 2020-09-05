from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    price = models.DecimalField(decimal_places=2, default=0.00, max_digits=16)
    description = models.CharField(max_length=255, null=True, blank=True, default='')
    image = models.ImageField(upload_to='products/images', default='')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()
