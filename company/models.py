from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=255)
    license_number = models.IntegerField()
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.CharField(max_length=400)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def get_absolute_url(self):
        return reverse('company-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
