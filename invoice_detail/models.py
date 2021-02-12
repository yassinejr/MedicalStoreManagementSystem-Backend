from django.db import models
from invoice.models import *
from medicine.models import *


# Create your models here.
class InvoiceDetail(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Invoice Detail"
        verbose_name_plural = "Invoices Details"