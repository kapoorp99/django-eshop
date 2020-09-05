from django.db import models


class ContactUsForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email
