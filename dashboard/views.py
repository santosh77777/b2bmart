from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from accounts.models import Account
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from .models import SellerProfile, Account, SellerStatutory, SellerBank
from accounts.views import is_seller, is_buyer
from .forms import SellerBankForm, SellerStatutoryForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/dashboard.html')

class SellerContactProfileView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def post(self,request, *args, **kwargs):
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        promoter_first_name =request.POST['promoter_first_name']
        promoter_last_name =request.POST['promoter_last_name']
        company =request.POST['company']
        designation =request.POST['designation']
        address_building =request.POST['address_building']
        address_area =request.POST['address_area']
        landmark =request.POST['landmark']
        locality =request.POST['locality']
        city =request.POST['city']
        state =request.POST['state']
        country =request.POST['country']
        pincode =request.POST['pincode']
        gstin =request.POST['gstin']
        company_website =request.POST['company_website']
        mobile =request.POST['mobile']
        alternative_mobile =request.POST['alternative_mobile']
        email =request.POST['email']
        alternative_email =request.POST['alternative_email']
        landline_no =request.POST['landline_no']
        alternative_landline_no =request.POST['alternative_landline_no']
        about_me =request.POST['about_me']

        user = User.objects.get(username=request.user.username)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        account = Account.objects.get(user=request.user)
        account.mobile = mobile
        account.state = state
        account.pincode = pincode
        account.company_name = company
        account.save()
        try:
            seller = SellerProfile.objects.filter(user=request.user)[0]
            if seller:
                seller.user = request.user
                seller.promoter_first_name = promoter_first_name
                seller.promoter_last_name = promoter_last_name
                seller.designation = designation
                seller.address_building = address_building
                seller.address_area = address_area
                seller.landmark = landmark
                seller.city = city
                seller.country = country
                seller.gstin = gstin
                seller.company_website = company_website
                seller.alternative_mobile = alternative_mobile
                seller.alternative_email = alternative_email
                seller.landline_no = landline_no
                seller.alternative_landline_no = alternative_landline_no
                seller.about_me = about_me
                seller.save()
                return redirect(".")
        except:
            seller = SellerProfile(user=request.user, promoter_first_name=promoter_first_name,
                promoter_last_name=promoter_last_name, designation=designation, address_building=address_building,
                address_area=address_area, 
                landmark=landmark, locality=locality, city=city,country=country,
                gstin=gstin, company_website=company_website, alternative_mobile=alternative_mobile,
                alternative_email=alternative_email, landline_no=landline_no, 
                alternative_landline_no=alternative_landline_no, about_me=about_me)
            seller.save()
            return redirect(".")

    def get(self,request, *args, **kwargs):

        account = Account.objects.get(user=request.user)
        try:
            seller = SellerProfile.objects.get(user=request.user)
            context = {'account': account,
                    'seller': seller
                    }
        except:
            context = {'account': account
                    }
        return render(request, 'dashboard/seller/contact_profile.html', context)


# class SellerBusinessProfileView(View):
#      def post(self,request, *args, **kwargs):
#             company_name =request.POST['company_name']
#             year_of_establishment =request.POST['year_of_establishment']
#             phone =request.POST['phone']
#             category ='type' in request.POST
#             annual_turnover =request.POST['annual_turnover']
#             company_card_front_view =request.POST['company_card_front_view']
#             company_card_back_view =request.POST['company_card_back_view']

#             business = BusinessProfile.objects.filter(user=request.user)[0]
#             if business:
#                 business.user = request.user
#                 business.company_name= company_name
#                 business. year_of_establishment =  year_of_establishment
#                 business.phone =phone
#                 business. category =  category
#                 business.annual_turnover = annual_turnover
#                 business.company_card_front_view = company_card_front_view
#                 business.company_card_back_view = company_card_back_view
#                 business.save()
#                 return redirect(".")
            
#             business = BusinessProfile(user=request.user, company_name=company_name,
#                         year_of_establishment=year_of_establishment, phone=phone,
#                         annual_turnover=annual_turnover, company_card_front_view=company_card_front_view, company_card_back_view =company_card_back_view)
#             business.save()
#             return redirect(".")

#      def get(self,request, *args, **kwargs):
#             business = BusinessProfile.objects.get(user=request.user)
#             context = {
#                          'business': business
#                         }
#             return render(request, 'dashboard/seller/business_profile.html')

class SellerStatutoryView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller
    def post(self,request, *args, **kwargs):
            try:
                statutory = SellerStatutory.objects.get(user=request.user)
                if statutory:
                    statutory.gst_no = request.POST['gst_no']
                    statutory.pan_no = request.POST['pan_no']
                    statutory.tan_no = request.POST['tan_no']
                    statutory.cin_no = request.POST['cin_no']
                    statutory.dgft_ie_code = request.POST['dgft_ie_code']
                    statutory.company_registration_no = request.POST['company_registration_no']
                    statutory.save()
            except:
                gst_no = request.POST['gst_no']
                pan_no = request.POST['pan_no']
                tan_no = request.POST['tan_no']
                cin_no = request.POST['cin_no']
                dgft_ie_code = request.POST['dgft_ie_code']
                company_registration_no = request.POST['company_registration_no']
                statutory = SellerStatutory(user=request.user, gst_no=gst_no,
                            pan_no=pan_no,tan_no=tan_no, cin_no=cin_no,
                            dgft_ie_code=dgft_ie_code,company_registration_no=company_registration_no)
                statutory.save()
                return redirect(".")
                
            return redirect(".")  

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/bank_details.html')
        


#Business Profile Seller Information Save


@login_required()
def SellerBusinessProfileView(request):
	seller = request.user.account
	form = BusinessProfileForm(instance= seller)

	if request.method == 'POST':
		form = BusinessProfileForm(request.POST, request.FILES, instance=seller)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'dashboard/seller/business_profile.html', context)

class SellerBankView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)
    
    def post(self,request, *args, **kwargs):
        form = SellerBankForm(request.POST)
        if form.is_valid:
            try:
                dilip = form.save(commit=False)
                dilip.user = request.user
                dilip.save()
                return redirect(".")
            except:
                seller_bank = SellerBank.objects.get(user=request.user)
                seller_bank.bank_name = form.cleaned_data['bank_name']
                seller_bank.account_no = form.cleaned_data['account_no']
                seller_bank.bank_account_name = form.cleaned_data['bank_account_name']
                seller_bank.ifsc_code = form.cleaned_data['ifsc_code']
                seller_bank.account_type = form.cleaned_data['account_type']

                seller_bank.alternative_bank_name = form.cleaned_data['alternative_bank_name']
                seller_bank.alternative_account_no = form.cleaned_data['alternative_account_no']
                seller_bank.alternative_bank_account_name = form.cleaned_data['alternative_bank_account_name']
                seller_bank.alternative_bank_ifsc_code = form.cleaned_data['alternative_bank_ifsc_code']
                seller_bank.alternative_bank_account_type = form.cleaned_data['alternative_bank_account_type']
                seller_bank.save()
                return redirect(".")                    

    def get(self,request, *args, **kwargs):
        try:
            seller_bank = SellerBank.objects.get(user=request.user)
            context= {'seller_bank':seller_bank}
        except:
            context = None
        return render(request, 'dashboard/seller/bank_details.html', context)
