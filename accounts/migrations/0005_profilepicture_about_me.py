# Generated by Django 2.2.15 on 2021-04-28 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210428_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepicture',
            name='about_me',
            field=models.TextField(blank=True),
        ),
    ]
