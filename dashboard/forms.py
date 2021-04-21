from django import forms
from .models import SellerBank, SellerStatutory

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

from product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['user']