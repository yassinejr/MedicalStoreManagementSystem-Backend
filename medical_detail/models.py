from django.db import models
from medicine.models import *


# Create your models here.
class Medical_detail(models.Model):
    name = models.CharField(max_length=255)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=255)
    salt_quantity = models.IntegerField()
    salt_quantity_type = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Medical Detail"
        verbose_name_plural = "Medical Details"