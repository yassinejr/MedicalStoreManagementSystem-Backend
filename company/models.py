from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    License_number = models.IntegerField()
    Address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.CharField(max_length=400)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
