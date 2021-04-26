from django.shortcuts import render, get_object_or_404
from . models import Product
from dashboard.models import SellerCompany
from django.views.generic import ListView
from django.contrib.auth.models import User

class HomeView(ListView):
    model = Product
    template_name = "index.html"

    def get_queryset(self):
        return Product.objects.filter(add_home=True)
        # return Product.objects.filter(user=user)
    

class HomeProductList(ListView):
    model = Product
    template_name = "dashboard/company.html"
    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     # return Product.objects.filter(add_home=True, user=user).first()

    #     return Product.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        
        context['object_list'] = Product.objects.filter(user=user)
        context['seller_company'] = SellerCompany.objects.filter(user=user)
        return context