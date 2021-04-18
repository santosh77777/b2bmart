from django.db import models
from accounts.models import Account
from django.contrib.auth.models import User

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    promoter_first_name = models.CharField(max_length=50)
    promoter_last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    address_building = models.CharField(max_length=100)
    address_area = models.CharField(max_length=100)
    landmark = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gstin = models.CharField(max_length=50)
    company_website = models.CharField(max_length=50)
    alternative_mobile = models.CharField(max_length=50)
    alternative_email = models.EmailField(max_length=50)
    landline_no = models.CharField(max_length=50)
    alternative_landline_no = models.CharField(max_length=50)
    about_me = models.TextField()

    def __str__(self):
        return self.user.first_name