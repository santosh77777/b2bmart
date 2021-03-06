# Generated by Django 2.2.15 on 2021-04-21 13:27

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
                ('unity_type', models.CharField(max_length=50)),
                ('min_order_quantity', models.IntegerField()),
                ('product_group', models.CharField(choices=[('Kitchen_stoves', 'Kitchen Stoves'), ('mixture_grinder', 'Mixture Grinder'), ('rice_cookers', 'Rice Cookers'), ('food_processors', 'Food Processors'), ('electric_mixers', 'Electric Mixers'), ('juicers', 'Juicers'), ('blenders', 'Blenders'), ('water_heaters', 'Water Heaters'), ('water_filters', 'Water Filters'), ('induction cookers', 'Induction Cookers'), ('exhaust_hoods', 'Exhaust Hoods'), ('sandwich_makers', 'Sandwich Makers'), ('toaster', 'Toaster'), ('deep_fryers', 'Deep Fryers'), ('dough_blenders', 'Dough Blenders'), ('coffee_makers', 'Coffee Makers'), ('electric_iron', 'Electric Iron'), ('vaccum_cleaner', 'Vaccum Cleaner'), ('air_purifiers', 'Air Purifiers'), ('trimmers_&_savers', 'Trimmer And Savers'), ('hair_drier', 'Hair Drier')], max_length=50)),
                ('description', models.TextField()),
                ('capacity', models.CharField(choices=[('200ml', '200 ml'), ('500ml', '500 ml'), ('1ltr', '1 ltr')], max_length=50)),
                ('material', models.CharField(choices=[('polycarbonate', 'Polycarbonate'), ('PET', 'PET'), ('other', 'Other')], max_length=50)),
                ('brand', models.CharField(choices=[('prestige', 'Prestige'), ('padmini', 'Padmini'), ('other', 'Other')], max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('product_type', models.CharField(max_length=50)),
                ('model_no', models.CharField(max_length=50)),
                ('power', models.CharField(max_length=50)),
                ('warranty', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
                ('neck_size', models.CharField(max_length=50)),
                ('closure_type', models.CharField(max_length=50)),
                ('product_code', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
