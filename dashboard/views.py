from django.shortcuts import render
from django.views.generic import View

class SellerDashboardView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/dashboard.html')

class SellerContactProfileView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/contact_profile.html')

class SellerBusinessProfileView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/business_profile.html')

class SellerStatutoryView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/statutory.html')

class SellerBankView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/bank_details.html')

