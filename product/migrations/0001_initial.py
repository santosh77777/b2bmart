# Generated by Django 2.2.15 on 2021-04-25 06:31

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
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('unity_type', models.CharField(blank=True, max_length=50, null=True)),
                ('min_order_quantity', models.IntegerField(blank=True, null=True)),
                ('product_group', models.CharField(blank=True, choices=[('Kitchen_stoves', 'Kitchen Stoves'), ('mixture_grinder', 'Mixture Grinder'), ('rice_cookers', 'Rice Cookers'), ('food_processors', 'Food Processors'), ('electric_mixers', 'Electric Mixers'), ('juicers', 'Juicers'), ('blenders', 'Blenders'), ('water_heaters', 'Water Heaters'), ('water_filters', 'Water Filters'), ('induction cookers', 'Induction Cookers'), ('exhaust_hoods', 'Exhaust Hoods'), ('sandwich_makers', 'Sandwich Makers'), ('toaster', 'Toaster'), ('deep_fryers', 'Deep Fryers'), ('dough_blenders', 'Dough Blenders'), ('coffee_makers', 'Coffee Makers'), ('electric_iron', 'Electric Iron'), ('vaccum_cleaner', 'Vaccum Cleaner'), ('air_purifiers', 'Air Purifiers'), ('trimmers_&_savers', 'Trimmer And Savers'), ('hair_drier', 'Hair Drier')], max_length=50, null=True)),
                ('description', models.TextField()),
                ('capacity', models.CharField(blank=True, max_length=50, null=True)),
                ('material', models.CharField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('model_no', models.CharField(blank=True, max_length=50, null=True)),
                ('power', models.CharField(blank=True, max_length=50, null=True)),
                ('warranty', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.CharField(blank=True, max_length=50, null=True)),
                ('neck_size', models.CharField(blank=True, max_length=50, null=True)),
                ('closure_type', models.CharField(blank=True, max_length=50, null=True)),
                ('product_code', models.CharField(blank=True, max_length=50, null=True)),
                ('packing_details', models.CharField(blank=True, max_length=50, null=True)),
                ('video_url', models.CharField(blank=True, max_length=50, null=True)),
                ('is_available', models.BooleanField(default=False)),
                ('image1', models.ImageField(default='', upload_to='products/')),
                ('image2', models.ImageField(default='', upload_to='products/')),
                ('image3', models.ImageField(default='', upload_to='products/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
