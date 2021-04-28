from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
# from b2bmart.utils import unique_slug_generator
from django.db.models.signals import pre_save
from .utils import generate_unique_slug


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    mobile = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    business_type = models.CharField(max_length=50, choices=BUSINESS_TYPE_CHOICES)
    nature_of_business = models.CharField(max_length=20, choices=NATURE_OF_BUSINESS_CHOICES)

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        if self.slug:
                  # edit
                if slugify(self.company_name) != self.slug:
                        self.slug = generate_unique_slug(Account, self.company_name)
        else: 
                         # create
                 self.slug = generate_unique_slug(Account, self.company_name)
        super(Account, self).save(*args, **kwargs)

    



