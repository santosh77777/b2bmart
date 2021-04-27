# Generated by Django 2.2.15 on 2021-04-26 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_add_home'),
        ('dashboard', '0003_auto_20210426_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellercompany',
            name='product',
        ),
        migrations.AddField(
            model_name='sellercompany',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AlterField(
            model_name='sellercompany',
            name='seller_bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.SellerBank'),
        ),
        migrations.AlterField(
            model_name='sellercompany',
            name='seller_statutory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.SellerStatutory'),
        ),
    ]
