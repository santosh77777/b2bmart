# Generated by Django 2.2.15 on 2021-04-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210428_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
