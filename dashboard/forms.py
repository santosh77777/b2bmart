from django import forms
from django.contrib.auth.models import User
from .models import *



class BusinessProfileForm(forms.ModelForm):
    CATEGORY = (
        ('Seller', 'Seller'),
        ('Manufacturer', 'Manufacturer'),
        ) 
    company_name =  forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))
    year_of_establishment = forms.DateField(widget=forms.DateInput(attrs={'class': "form-control"}))
    phone =  forms.CharField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    category = forms.ChoiceField(choices = CATEGORY, widget=forms.Select(attrs={'class': "form-control"}))
    annual_turnover =  forms.DecimalField(widget=forms.TextInput(attrs={'class': "form-control"}))
    company_card_front_view = forms.ImageField(widget=forms.FileInput(attrs={'class': ""}), required=False)
    company_card_back_view = forms.ImageField(widget=forms.FileInput(attrs={'class': ""}), required=False)
    class Meta:
        model = BusinessProfile
        fields = '__all__'
       
