from django.db import models
from company.models import *


# Create your models here.
class CompanyAccount(models.Model):
    choices = (("Debit", "Debit"), ("Credit", "Credit"), ("Cash", "Cash"), ("Check", "Check"))

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=choices, max_length=20)
    transaction_amount = models.IntegerField()
    transaction_date = models.DateField(auto_now_add=True)
    payment_mode = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Company Account"
        verbose_name_plural = "Company Accounts"
