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

class BusinessProfile(models.Model):
    CATEGORY = (
			('Seller', 'Seller'),
			('Manufacturer', 'Manufacturer'),
			) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='businessprofile')
    company_name = models.CharField(max_length=200, null=True)
    year_of_establishment = models.DateField(null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    annual_turnover = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    company_card_front_view = models.ImageField(upload_to='images/', null=True, blank=True)
    company_card_back_view = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.user.username
      
class SellerBusinessProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # cimpany_name = models.CharField(max_length=50)
    # year_of_establishment = models.DateField(auto_now_add=True)
    # additional_contact_name = models.CharField(max_length=50)
    # Manufacturer = models.CharField(max_length=100)
    # annual_turnover = models.CharField(max_length=100)
    # b2b_mart_catalog_uri = models.URLField(max_length=50)
    # company_card_front_view = models.CharField(max_length=50)
    # company_card_back_view = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.user.first_name 
    #     Statutory
    pass
class SellerStatutory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gst_no = models.CharField(max_length=50, null=True)
    pan_no = models.CharField(max_length=50, null=True)
    tan_no = models.CharField(max_length=50, null=True)
    cin_no = models.CharField(max_length=100, null=True)
    dgft_ie_code = models.CharField(max_length=100, null=True)
    company_registration_no = models.URLField(max_length=50, null=True)

    def __str__(self):
        return self.user.first_name 
    

class SellerBank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    bank_account_name = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    alternative_bank_name = models.CharField(max_length=50)
    alternative_account_no = models.CharField(max_length=50)
    alternative_bank_account_name = models.CharField(max_length=50)
    alternative_bank_ifsc_code = models.CharField(max_length=50)
    alternative_bank_account_type = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name 
