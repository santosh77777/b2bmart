from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_save
# from b2bmart.utils import unique_slug_generator


BUSINESS_TYPE_CHOICES = (
        ('Seller', 'Seller'),
        ('Buye', 'Buye'),
        ('Logistic_Advertisement', 'Logistic Advertisement'),
)

NATURE_OF_BUSINESS_CHOICES = (
        ('Manufacturer', 'Manufacturer'),
        ('Retailer', 'Retailer'),
        ('Distributer', 'Distributer'),
        ('Wholeseller', 'Wholeseller'),
        ('Exporter', 'Exporter'),
)


class Account(models.Model):
#     slug = models.SlugField(max_length=250, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    mobile = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    business_type = models.CharField(max_length=50, choices=BUSINESS_TYPE_CHOICES)
    nature_of_business = models.CharField(max_length=20, choices=NATURE_OF_BUSINESS_CHOICES)

    def __str__(self):
        return str(self.user)


# def slug_generator(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)


# pre_save.connect(slug_generator, sender=Account)
