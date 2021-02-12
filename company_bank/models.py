from django.db import models
from company.models import *


# Create your models here.
class Company_bank(models.Model):
    bank_account_number = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=255)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Company Bank"
        verbose_name_plural = "Companies Bank"