from django.shortcuts import render, get_object_or_404, redirect
from . models import Product
from dashboard.models import SellerCompany, BusinessProfile
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import HttpResponse
from accounts.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
id_brand=[]
id_category=[]
def HomeView(request):
    brand=[]
    brand_id=[]
    cat=[]
    cat_id_obj=[]
    prd=Product.objects.all()
    for i in prd:
        if(i.brand not in brand):
            brand.append(i.brand)
            brand_id.append(i.id)
        if(i.product_group not in cat):
            cat.append(i.product_group)
            cat_id_obj.append(i.id)
    
    brand=json.dumps(list(brand))
    brand_id=json.dumps(list(brand_id))
    cat_data=json.dumps(list(cat))
    cat_id=json.dumps(list(cat_id_obj))

    if request.is_ajax():
        global id_brand
        global id_category
        id_brand=request.POST.getlist('brand[]')
        id_category=request.POST.getlist('cat[]')
        print(id_brand)
        print(id_category)
    
    object_list=Product.objects.filter(add_home=True).order_by("?")[:8]
    x = list(object_list)
    l = len(x)
    i=0
    while(l%4!=0):
        x.append(x[i])
        l=l+1
        i=i+1


    context={'brand_data':brand,
             'brand_id':brand_id,
             'x':x,  
             'cat_data':cat_data,
             'cat_id':cat_id,                           
             }
    return render(request,'index.html',  context)
    
        
def category(request):
    if request.is_ajax():
        global id_brand
        global id_category
        id_brand=request.POST.getlist('brand[]')
        id_category=request.POST.getlist('cat[]')
    show_res=[]
    queryset=[]
    print("cat",id_brand)
    if(len(id_brand)>0):
        show_res=id_brand
    elif(len(id_category)>0):
        show_res=id_category
    temp=[]
    temp=show_res
    show_res=[]
    for i in temp:
        show_res.append(i.replace("category",""))

    show_res=list(dict.fromkeys(show_res))
    
    for i in show_res:
        product_detail=Product.objects.filter(id=i)
        queryset.append(product_detail)


    brand=[]
    brand_id=[]
    cat=[]
    cat_id_obj=[]
    prd=Product.objects.all()
    for i in prd:
        if(i.brand not in brand):
            brand.append(i.brand)
            brand_id.append(i.id)
        if(i.product_group not in cat):
            cat.append(i.product_group)
            cat_id_obj.append(i.id)
    
    brand=json.dumps(list(brand))
    brand_id=json.dumps(list(brand_id))
    cat_data=json.dumps(list(cat))
    cat_id=json.dumps(list(cat_id_obj))


    context={"search_product":queryset,
             'brand_data':brand,
             'brand_id':brand_id,
             'cat_data':cat_data,
             'cat_id':cat_id
            }
    return render(request,'category.html',context)

################################## this is for displaying the home page ################################## 
# class HomeView(ListView):
#     model = Product
#     template_name = "index.html"

    # def get_queryset(self):
        # return Product.objects.filter(add_home=True)
    #     # return Product.objects.raw('SELECT  DISTINCT user_id from product_product WHERE add_home=True')
    #     return Product.objects.order_by('user_id').values_list('user_id', flat=True).distinct()
    
class WebsiteHomeList(ListView):
    model = Product
    template_name = "dashboard/company.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = get_object_or_404(User, account__slug=self.kwargs.get("slug"))
        
        # context['object_list'] = Product.objects.filter(user=user)
        context['object_list'] = Product.objects.filter(user=user, arrange=True)
        context['all_object_list'] = Product.objects.filter(user=user)
        context['seller_company'] = SellerCompany.objects.filter(user=user)
        context['business_profile'] = BusinessProfile.objects.filter(user=user)
        return context
        

