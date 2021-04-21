from django.db import models
from django.contrib.auth.models import User

PRODUCT_GROUP_CHOICES = (
    ("Kitchen_stoves", "Kitchen Stoves"),
    ("mixture_grinder", "Mixture Grinder"),
    ("rice_cookers", "Rice Cookers"),
    ("food_processors", "Food Processors"),
    ("electric_mixers", "Electric Mixers"),
    ("juicers", "Juicers"),
    ("blenders", "Blenders"),
    ("water_heaters", "Water Heaters"),
    ("water_filters", "Water Filters"),
    ("induction cookers", "Induction Cookers"),
    ("exhaust_hoods", "Exhaust Hoods"),
    ("sandwich_makers", "Sandwich Makers"),
    ("toaster", "Toaster"),
    ("deep_fryers", "Deep Fryers"),
    ("dough_blenders", "Dough Blenders"),
    ("coffee_makers", "Coffee Makers"),
    ("electric_iron", "Electric Iron"),
    ("vaccum_cleaner", "Vaccum Cleaner"),
    ("air_purifiers", "Air Purifiers"),
    ("trimmers_&_savers", "Trimmer And Savers"),
    ("hair_drier", "Hair Drier"),
    )

CAPACITY_CHOICES = (
    ("200ml", "200 ml"),
    ("500ml", "500 ml"),
    ("1ltr", "1 ltr")
)

MATERIAL_CHOICES = (
    ("polycarbonate", "Polycarbonate"),
    ("PET", "PET"),
    ("other", "Other")
)

Brand_CHOICES = (
    ("prestige", "Prestige"),
    ("padmini", "Padmini"),
    ("other", "Other")
)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    unity_type = models.CharField(max_length=50, null=True,blank=True)
    min_order_quantity = models.IntegerField(null=True,blank=True)
    product_group = models.CharField(max_length=50, choices=PRODUCT_GROUP_CHOICES, null=True,blank=True)
    description = models.TextField()
    capacity = models.CharField(max_length=50, choices=CAPACITY_CHOICES, null=True,blank=True)
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES, null=True,blank=True)
    brand = models.CharField(max_length=50, choices=Brand_CHOICES, null=True,blank=True)
    color = models.CharField(max_length=50, null=True,blank=True)
    size = models.CharField(max_length=50, null=True,blank=True)
    product_type = models.CharField(max_length=50, null=True,blank=True)
    model_no = models.CharField(max_length=50, null=True,blank=True)
    power = models.CharField(max_length=50, null=True,blank=True)
    warranty = models.CharField(max_length=50, null=True,blank=True)
    rating = models.CharField(max_length=50, null=True,blank=True)
    neck_size = models.CharField(max_length=50, null=True,blank=True)
    closure_type = models.CharField(max_length=50, null=True,blank=True)
    product_code = models.CharField(max_length=50, null=True,blank=True)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.user
    
