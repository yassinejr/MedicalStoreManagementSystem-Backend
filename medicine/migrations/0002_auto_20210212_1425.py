# Generated by Django 3.1.6 on 2021-02-12 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'verbose_name': 'Medicine', 'verbose_name_plural': 'Medicines'},
        ),
    ]