# Generated by Django 3.2 on 2021-04-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210417_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='business_type',
            field=models.CharField(choices=[('Seller', 'Seller'), ('Buye', 'Buye'), ('Logistic_Advertisement', 'Logistic Advertisement')], max_length=50),
        ),
    ]
