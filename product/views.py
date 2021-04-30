from django.shortcuts import render, get_object_or_404
from . models import Product
from dashboard.models import SellerCompany, BusinessProfile
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import HttpResponse
from accounts.models import *
import json
id_brand=[]
def HomeView(request):
    brand=Product.objects.values_list('brand', flat=True)
    brand_id=Product.objects.values_list('id',flat=True)
    brand=json.dumps(list(brand))
    brand_id=json.dumps(list(brand_id))
    if request.is_ajax():
        global id_brand
        id_brand=request.POST.getlist('brand[]')
        print(id_brand)
        return HttpResponse('success') 
    object_list=Product.objects.filter(add_home=True)
    context={'brand_data':brand,
             'brand_id':brand_id,
             'object_list':object_list
             }
    return render(request,'index.html',  context)
    
        
def category(request):
    print("cat")
    show_brand=[]
    queryset=[]
    for i in id_brand:
        productt= Product.objects.get(id=i)
        show_brand.append(productt.brand)
    print("show_brand",show_brand)
    for i in show_brand:
        product_detail=Product.objects.filter(brand=i)
        queryset.append(product_detail)
    
    context={"search_product":queryset}
    return render(request,'category.html',context)

################################## this is for displaying the home page ################################## 
# class HomeView(ListView):
#     model = Product
#     template_name = "index.html"

    # def get_queryset(self):
        # return Product.objects.filter(add_home=True)
    #     # return Product.objects.raw('SELECT  DISTINCT user_id from product_product WHERE add_home=True')
    #     return Product.objects.order_by('user_id').values_list('user_id', flat=True).distinct()
    
class HomeProductList(ListView):
    model = Product
    template_name = "dashboard/company.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = get_object_or_404(User, account__slug=self.kwargs.get("slug"))
        
        context['object_list'] = Product.objects.filter(user=user)
        context['seller_company'] = SellerCompany.objects.filter(user=user)
        context['business_profile'] = BusinessProfile.objects.filter(user=user)
        return context
        

