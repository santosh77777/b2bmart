from django.shortcuts import render, get_object_or_404
from . models import Product
from dashboard.models import SellerCompany
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
id_brand=[]
def HomeView(request):
    print("YEs")
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
    # data = list(object_list.values())
    print(type(object_list))
        # name.append(i.user)
    context={'brand_data':brand,
             'brand_id':brand_id,
             'object_list':object_list,
             
             }
    return render(request,'index.html',  context)
    
        
def category(request):
    print("category")
    print(id_brand)
    return render(request,'category.html')

        
    # def get_context_data(self, **kwargs):
            
    #     # Call the base implementation first to get a context
    #     context = super().get_queryset(**kwargs)
        
    #     # context['brand']=Product.objects.filter('brand', flat=True)
    #     # context['brand_id']=Product.objects.filter('id',flat=True)
    #     # print(context)
        
    #     # brand=json.dumps(list(brand))
    #     # brand_id=json.dumps(list(brand_id))
        
    #     return context
    #     # return Product.objects.filter(user=user)
    

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
        