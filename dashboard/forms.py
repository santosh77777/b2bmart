from django import forms
from .models import *
from product.models import Product
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
    year_of_establishment = forms.DateField( localize=True, widget=forms.DateInput(format = '%Y-%m-%d', attrs={'class': 'form-control', 'type':'date'}), required=True)
    phone = forms.IntegerField(widget=forms.NumberInput( attrs={'class': 'form-control'}), required=True)
    category = forms.ChoiceField(initial='Select Value', widget=forms.Select( attrs={'class': 'form-control'}), choices=CATEGORY,  required=True)
    annual_turnover = forms.IntegerField(widget=forms.NumberInput( attrs={'class': 'form-control'}), required=True)
    company_card_front_view = forms.ImageField(widget=forms.FileInput( attrs={'class': ''}), required=False)
    company_card_back_view = forms.ImageField(widget=forms.FileInput( attrs={'class': ''}), required=False)

    class Meta:
        model = BusinessProfile
        fields = "__all__"
        exclude = ['user']



# class SellerManageProductViewForm(forms.ModelForm):
#      class Meta:
#         model = Product
#         fields = "__all__"
#         exclude = ['user']
