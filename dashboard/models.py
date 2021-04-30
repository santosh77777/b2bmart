from django.db import models
from accounts.models import Account
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from product.models import Product


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
        return self.user.username



def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


class BusinessProfile(models.Model):
    CATEGORY = (
			('Seller', 'Seller'),
			('Manufacturer', 'Manufacturer'),
			) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='businessprofile')
    company_name = models.CharField(max_length=200, blank=True, null=True)
    year_of_establishment = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
    annual_turnover = models.CharField(max_length=200, blank=True, null=True)
    company_card_front_view = models.ImageField(default="company_card.png", upload_to='images/', validators=[validate_image], null=True, blank=True, help_text='Maximum file size allowed is 2Mb')
    company_card_back_view = models.ImageField(default="company_card.png", upload_to='images/', validators=[validate_image], null=True, blank=True, help_text='Maximum file size allowed is 2Mb')
    
    def __str__(self):
        return self.user.username

      
class SellerStatutory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gst_no = models.CharField(max_length=50, null=True)
    pan_no = models.CharField(max_length=50, null=True)
    tan_no = models.CharField(max_length=50, null=True)
    cin_no = models.CharField(max_length=100, null=True)
    dgft_ie_code = models.CharField(max_length=100, null=True)
    company_registration_no = models.URLField(max_length=50, null=True)

    def __str__(self):
        return self.user.username
    

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
        return self.user.username



from django.db.models.signals import post_save
def businessprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = BusinessProfile.objects.create(user=instance)


post_save.connect(businessprofile_receiver, sender=User)

class SellerCompany(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sellercompany')
    about_seller = models.TextField(blank=True, null=True)
    no_of_employees = models.PositiveIntegerField(blank=True, null=True)
    legal_status_of_firm = models.CharField(max_length=50)
    catalogue = models.FileField(upload_to="files/seller_catalogues", blank=True, null=True)
    branded_video = EmbedVideoField()
    caption = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(default="company_card.png", upload_to="images/seller_logos")
    banner_image =models.ImageField(default="company_card.png", upload_to="images/seller_banner_images")
     
    def __str__(self):
        return self.user.username


def sellercompany_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = SellerCompany.objects.create(user=instance)

post_save.connect(sellercompany_receiver, sender=User)

BUSINESS_TYPE_CHOICES = (
        ('Manufacturer', 'Manufacturer'),
        ('Retailer', 'Retailer'),
        ('Distributer', 'Distributer'),
        ('Wholeseller', 'Wholeseller'),
        ('Exporter', 'Exporter'),
)
class ShareDetail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPE_CHOICES)
    message = models.TextField()
    send_copy = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.name) 
