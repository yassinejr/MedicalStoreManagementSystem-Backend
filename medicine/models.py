from django.db import models
from company.models import *


# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=255)
    medical_type = models.CharField(max_length=255)
    buy_price = models.DecimalField(max_digits=8, decimal_places=3)
    sell_price = models.DecimalField(max_digits=8, decimal_places=3)
    taxes = models.DecimalField(max_digits=8, decimal_places=3)
    batch_number = models.DecimalField(max_digits=8, decimal_places=3) #
    shelf = models.DecimalField(max_digits=8, decimal_places=3)
    expire_date = models.DateField()
    manufacture_date = models.DateField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    in_stock_total = models.IntegerField()
    quantity_in_strip = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"

