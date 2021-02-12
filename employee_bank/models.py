from django.db import models
from employee.models import *


# Create your models here.
class EmployeeBank(models.Model):
    bank_account_number = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=255)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Employee Bank"
        verbose_name_plural = "Employees Banks"