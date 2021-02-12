# Generated by Django 3.1.6 on 2021-02-12 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('salt_name', models.CharField(max_length=255)),
                ('salt_quantity', models.IntegerField()),
                ('salt_quantity_type', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=400)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
            ],
        ),
    ]