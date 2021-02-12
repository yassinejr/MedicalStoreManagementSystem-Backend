from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"