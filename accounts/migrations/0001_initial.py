# Generated by Django 2.2.15 on 2021-04-21 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
                ('business_type', models.CharField(choices=[('Seller', 'Seller'), ('Buye', 'Buye'), ('Logistic_Advertisement', 'Logistic Advertisement')], max_length=50)),
                ('nature_of_business', models.CharField(choices=[('Manufacturer', 'Manufacturer'), ('Retailer', 'Retailer'), ('Distributer', 'Distributer'), ('Wholeseller', 'Wholeseller'), ('Exporter', 'Exporter')], max_length=20)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
