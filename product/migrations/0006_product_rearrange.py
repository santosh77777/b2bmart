# Generated by Django 2.2.15 on 2021-04-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rearrange',
            field=models.BooleanField(default=False),
        ),
    ]
