# Generated by Django 2.2.15 on 2021-04-22 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210422_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
    ]