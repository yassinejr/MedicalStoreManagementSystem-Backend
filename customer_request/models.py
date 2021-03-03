from django.db import models

# Create your models here.
from rest_framework.reverse import reverse


class CustomerRequest(models.Model):
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    medicine_detail = models.CharField(max_length=255)
    status =models.BooleanField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Customer Request"
        verbose_name_plural = "Customer Requests"

    def get_absolute_url(self):
        return reverse('customer-request-detail', args=[str(self.id)])

    def __str__(self):
        return self.customer_name