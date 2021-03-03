from django.db import models
from rest_framework.reverse import reverse


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
