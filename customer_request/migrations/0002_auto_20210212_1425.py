# Generated by Django 3.1.6 on 2021-02-12 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerrequest',
            options={'verbose_name': 'Customer Request', 'verbose_name_plural': 'Customer Requests'},
        ),
    ]