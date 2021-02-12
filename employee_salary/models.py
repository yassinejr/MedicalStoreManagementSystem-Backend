from django.db import models
from employee.models import *


# Create your models here.
class Employee_Salary(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_amount = models.IntegerField()
    salary_date = models.DateField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Employee Salary"
        verbose_name_plural = "Employees Salaries"