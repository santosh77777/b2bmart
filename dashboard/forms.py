from django import forms
from .models import *
from product.models import Product
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
class SellerBankForm(forms.ModelForm):
    class Meta:
        model = SellerBank
        fields = ['bank_name', 'account_no', 'bank_account_name', 'ifsc_code', 
        'account_type', 'alternative_bank_name', 'alternative_account_no', 
        'alternative_bank_account_name', 'alternative_bank_ifsc_code', 'alternative_bank_account_type']

class SellerStatutoryForm(forms.ModelForm):
    class Meta:
        model = SellerStatutory
        fields = ['gst_no', 'pan_no', 'tan_no', 'cin_no', 'dgft_ie_code', 'company_registration_no']


        


class BusinessProfileForm(forms.ModelForm):
    CATEGORY = (
			('Seller', 'Seller'),
			('Manufacturer', 'Manufacturer'),
			) 
    company_name = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control'}), required=True)
    year_of_establishment = forms.DateField( localize=True, widget=forms.DateInput(format = '%Y-%m-%d', attrs={'class': '', 'type':'date'}), required=True)
    phone = forms.IntegerField(widget=forms.NumberInput( attrs={'class': 'form-control'}), required=True)
    category = forms.ChoiceField(initial='Select Value', widget=forms.Select( attrs={'class': 'form-control'}), choices=CATEGORY,  required=True)
    annual_turnover = forms.IntegerField(widget=forms.NumberInput( attrs={'class': 'form-control'}), required=True)
    company_card_front_view = forms.ImageField(widget=forms.FileInput( attrs={'class': ''}), required=False)
    company_card_back_view = forms.ImageField(widget=forms.FileInput( attrs={'class': ''}), required=False)

    class Meta:
        model = BusinessProfile
        fields = "__all__"
        exclude = ['user']


class SellerCompanyForm(forms.ModelForm):
    about_seller = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control','name':'about', 'id':'about_seller'}), required=True)
    no_of_employees = forms.IntegerField(widget=forms.NumberInput( attrs={'class': 'form-control','name':'num', 'id':'noofemployees'}), required=True)
    legal_status_of_firm = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control','name':'legal', 'id':'legal_status_of_firm'}), required=True)
    catalogue = forms.FileField(widget=forms.FileInput( attrs={'class': 'form-control','name':'catalogue','id':"catalogue"}), required=False)
    branded_video = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'name':'video' ,'id':"branded_video"}), required=True)
    logo = forms.ImageField(widget=forms.FileInput( attrs={'class': 'form-control','name':'logo','id':'logo'}), required=False)
    banner_image = forms.ImageField(widget=forms.FileInput( attrs={'class': 'form-control','name':'banner','id':'banner'}), required=False)

    class Meta:
        model = SellerCompany
        fields = "__all__"
        exclude = ['user']



class SellerSingleProductViewForm(forms.ModelForm):
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
    name = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=True)
    price = forms.IntegerField(widget=forms.NumberInput( attrs={'class': 'form-control', 'id':''}), required=True)
    unit_type = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    min_order_quantity = forms.IntegerField(widget=forms.NumberInput( attrs={'class': 'form-control', 'id':''}), required=False)
    product_group = forms.ChoiceField(initial='Select Value', widget=forms.Select( attrs={'class': 'form-control'}), choices=PRODUCT_GROUP_CHOICES,  required=True)
    description = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=True)
    capacity = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    material = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    brand = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':'brand', 'name':'brand'}), required=True)
    color = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    size = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    model_no = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    power = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    warranty = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=True)
    neck_size = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    closure_type = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    product_code = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=True)
    packing_details = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)
    rating = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'id':''}), required=False)

    video_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control',  'id':""}), required=False)
    image1 = forms.ImageField(widget=forms.FileInput( attrs={'class': 'form-control'}), required=False)
    image2 = forms.ImageField(widget=forms.FileInput( attrs={'class': 'form-control'}), required=False)
    image3 = forms.ImageField(widget=forms.FileInput( attrs={'class': 'form-control'}), required=False)


    class Meta:
        model = Product
        fields = ['name', 'price', 'unit_type', 'min_order_quantity', 'product_group', 'description', 
        'description', 'capacity','material','brand','color','size', 'model_no', 'power', 'warranty', 'neck_size', 'closure_type', 'product_code', 'packing_details','rating'
          ,'video_url', 'is_available', 'image1', 'image2', 'image3', 'arrange', 'add_home' ]
        


PAYMENT_CHOICES = (
    ('C', 'COD'),
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


