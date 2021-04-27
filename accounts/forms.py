from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='first_name')
    last_name = forms.CharField(max_length=30, label='last_name')

    email = forms.EmailField(max_length=30, label='email')
    mobile = forms.CharField(max_length=10, label='mobile')   

    state = forms.CharField(max_length=20)
    pincode = forms.CharField(max_length=20)
    company_name = forms.CharField(max_length=20)
    business_type = forms.CharField(max_length=20)
    nature_of_business = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile', 'state', 'pincode', 'company_name', 'business_type', 'nature_of_business']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
       
        
        up = user.account
        up.mobile = self.cleaned_data['mobile']
        up.state = self.cleaned_data['state']
        up.pincode = self.cleaned_data['pincode']
        up.company_name = self.cleaned_data['company_name']
        up.business_type = self.cleaned_data['business_type']
        up.nature_of_business = self.cleaned_data['nature_of_business']
        email = self.cleaned_data['email']
        try:
            user_email = email
            validate_email( user_email )
            return True
        except ValidationError:
            return user_email
    
        user.email = user_email

        user.save()
        up.save()



        

    
   

    


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
