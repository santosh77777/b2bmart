# Generated by Django 2.2.15 on 2021-04-18 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_sellerprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
        ),
    ]