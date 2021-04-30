# Generated by Django 2.2.15 on 2021-04-28 13:12

import dashboard.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerStatutory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst_no', models.CharField(max_length=50, null=True)),
                ('pan_no', models.CharField(max_length=50, null=True)),
                ('tan_no', models.CharField(max_length=50, null=True)),
                ('cin_no', models.CharField(max_length=100, null=True)),
                ('dgft_ie_code', models.CharField(max_length=100, null=True)),
                ('company_registration_no', models.URLField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promoter_first_name', models.CharField(max_length=50)),
                ('promoter_last_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('address_building', models.CharField(max_length=100)),
                ('address_area', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('gstin', models.CharField(max_length=50)),
                ('company_website', models.CharField(max_length=50)),
                ('alternative_mobile', models.CharField(max_length=50)),
                ('alternative_email', models.EmailField(max_length=50)),
                ('landline_no', models.CharField(max_length=50)),
                ('alternative_landline_no', models.CharField(max_length=50)),
                ('about_me', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellerCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_seller', models.TextField(blank=True, null=True)),
                ('no_of_employees', models.PositiveIntegerField(blank=True, null=True)),
                ('legal_status_of_firm', models.CharField(max_length=50)),
                ('catalogue', models.FileField(blank=True, null=True, upload_to='files/seller_catalogues')),
                ('branded_video', embed_video.fields.EmbedVideoField()),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.ImageField(default='company_card.png', upload_to='images/seller_logos')),
                ('banner_image', models.ImageField(default='company_card.png', upload_to='images/seller_banner_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sellercompany', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellerBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50)),
                ('account_no', models.CharField(max_length=50)),
                ('bank_account_name', models.CharField(max_length=50)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('account_type', models.CharField(max_length=50)),
                ('alternative_bank_name', models.CharField(max_length=50)),
                ('alternative_account_no', models.CharField(max_length=50)),
                ('alternative_bank_account_name', models.CharField(max_length=50)),
                ('alternative_bank_ifsc_code', models.CharField(max_length=50)),
                ('alternative_bank_account_type', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('year_of_establishment', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, choices=[('Seller', 'Seller'), ('Manufacturer', 'Manufacturer')], max_length=200, null=True)),
                ('annual_turnover', models.CharField(blank=True, max_length=200, null=True)),
                ('company_card_front_view', models.ImageField(blank=True, default='company_card.png', help_text='Maximum file size allowed is 2Mb', null=True, upload_to='images/', validators=[dashboard.models.validate_image])),
                ('company_card_back_view', models.ImageField(blank=True, default='company_card.png', help_text='Maximum file size allowed is 2Mb', null=True, upload_to='images/', validators=[dashboard.models.validate_image])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='businessprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
