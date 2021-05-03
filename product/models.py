from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

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
    ("induction_cookers", "Induction Cookers"),
    ("exhaust_hoods", "Exhaust Hoods"),
    ("sandwich_makers", "Sandwich Makers"),
    ("toaster", "Toaster"),
    ("deep_fryers", "Deep Fryers"),
    ("dough_blenders", "Dough Blenders"),
    ("coffee_makers", "Coffee Makers"),
    ("electric_iron", "Electric Iron"),
    ("vaccum_cleaner", "Vaccum Cleaner"),
    ("air_purifiers", "Air Purifiers"),
    ("trimmers_and_savers", "Trimmer And Savers"),
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
    discount_price = models.FloatField(blank=True, null=True)
    unity_type = models.CharField(max_length=50, null=True,blank=True)
    min_order_quantity = models.IntegerField(null=True,blank=True)
    product_group = models.CharField(max_length=50, choices=PRODUCT_GROUP_CHOICES, null=True,blank=True)
    description = models.TextField()
    capacity = models.CharField(max_length=50, null=True,blank=True)
    material = models.CharField(max_length=50, null=True,blank=True)
    brand = models.CharField(max_length=50, null=True,blank=True)
    color = models.CharField(max_length=50, null=True,blank=True)
    size = models.CharField(max_length=50, null=True,blank=True)
    model_no = models.CharField(max_length=50, null=True,blank=True)
    power = models.CharField(max_length=50, null=True,blank=True)
    warranty = models.CharField(max_length=50, null=True,blank=True)
    rating = models.CharField(max_length=50, null=True,blank=True)
    neck_size = models.CharField(max_length=50, null=True,blank=True)
    closure_type = models.CharField(max_length=50, null=True,blank=True)
    product_code = models.CharField(max_length=50, null=True,blank=True)
    packing_details = models.CharField(max_length=50, null=True,blank=True)
    video_url = models.CharField(max_length=50, null=True,blank=True)
    is_available = models.BooleanField(default=False,null=True,blank=True)
    image1=models.ImageField(upload_to="products/",default='')
    image2=models.ImageField(upload_to="products/",default='')
    image3=models.ImageField(upload_to="products/",default='')
    arrange = models.BooleanField(default=False)
    add_home = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("dashboard:seller_product_detail", kwargs={
            'pk': self.pk
        })

    def get_add_to_cart_url(self):
        return reverse("dashboard:add-to-cart", kwargs={
            'pk': self.pk
        })

    def get_remove_from_cart_url(self):
        return reverse("dashboard:remove-from-cart", kwargs={
            'pk': self.pk
        })


class OrderProduct(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True,blank=True)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_product_price(self):
        return self.quantity * self.product.price

    def get_total_discount_product_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_total_discount_product_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_product_price()
        return self.get_total_product_price()


class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True,blank=True)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.get_final_price()
        return total