from django.shortcuts import render, redirect
from django.views.generic import View
from accounts.models import Account
from django.contrib.auth.models import User
from .models import SellerProfile, Account
from django.contrib import messages

class SellerDashboardView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/dashboard.html')

class SellerContactProfileView(View):
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
        print("aboutttttttttttttttt", about_me)  
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
        
        seller = SellerProfile(user=request.user, promoter_first_name=promoter_first_name,
            promoter_last_name=promoter_last_name, designation=designation, address_building=address_building,
            address_area=address_area, 
            landmark=landmark, locality=locality, city=city, pincode=pincode,
            gstin=gstin, company_website=company_website, alternative_mobile=alternative_mobile,
            alternative_email=alternative_email, landline_no=landline_no, 
            alternative_landline_no=alternative_landline_no, about_me=about_me)
        seller.save()
        return redirect(".")

    def get(self,request, *args, **kwargs):
        account = Account.objects.get(user=request.user)
        seller = SellerProfile.objects.get(user=request.user)
        context = {'account': account,
                   'seller': seller
                   }
        return render(request, 'dashboard/seller/contact_profile.html', context)

class SellerBusinessProfileView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/business_profile.html')

class SellerStatutoryView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/statutory.html')

class SellerBankView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/bank_details.html')

