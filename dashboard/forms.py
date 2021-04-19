from django import forms
from django.contrib.auth.models import User
from .models import *



class BusinessProfileForm(forms.ModelForm):
    company_name =  forms.CharField(label='COmpany Name',  widget=forms.TextInput(attrs={'class': "form-control"}))
    phone =  forms.CharField(label='Contact Number',widget=forms.TextInput(attrs={'class': "form-control"}))
    annual_turnover =  forms.CharField(label='Annual Turnover', widget=forms.TextInput(attrs={'class': "form-control"}))
    
    class Meta:
        model = BusinessProfile
        fields = '__all__'
