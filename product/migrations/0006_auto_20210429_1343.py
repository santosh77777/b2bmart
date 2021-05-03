# Generated by Django 2.2.15 on 2021-04-29 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_delete_eshopeform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Kitchen_stoves', 'Kitchen Stoves'), ('mixture_grinder', 'Mixture Grinder'), ('rice_cookers', 'Rice Cookers'), ('food_processors', 'Food Processors'), ('electric_mixers', 'Electric Mixers'), ('juicers', 'Juicers'), ('blenders', 'Blenders'), ('water_heaters', 'Water Heaters'), ('water_filters', 'Water Filters'), ('induction cookers', 'Induction Cookers'), ('exhaust_hoods', 'Exhaust Hoods'), ('sandwich_makers', 'Sandwich Makers'), ('toaster', 'Toaster'), ('deep_fryers', 'Deep Fryers'), ('dough_blenders', 'Dough Blenders'), ('coffee_makers', 'Coffee Makers'), ('electric_iron', 'Electric Iron'), ('vaccum_cleaner', 'Vaccum Cleaner'), ('air_purifiers', 'Air Purifiers'), ('trimmers_&_savers', 'Trimmer And Savers'), ('hair_drier', 'Hair Drier')], max_length=50, null=True)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_group',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category'),
        ),
    ]
