# Generated by Django 2.2.15 on 2021-04-25 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_arrange'),
        ('dashboard', '0003_auto_20210425_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellercompany',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
