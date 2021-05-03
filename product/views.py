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
from django.contrib import messages
from django.views import View
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse

id_brand=[]
id_category=[]

def HomeView(request):
    if request.method =='POST' and request.POST['action']=='send_var':
        loc=request.POST.get('alt')
        print(loc)
        nav_prd=Product.objects.filter(name=loc)
    brand=[]
    brand_id=[]
    cat=[]
    cat_id_obj=[]
    prd_name=[]
    prd=Product.objects.all()
    for i in prd:
        if(i.brand not in brand):
            brand.append(i.brand)
            brand_id.append(i.id)
        if(i.product_group not in cat):
            cat.append(i.product_group)
            cat_id_obj.append(i.id)
        if(i.name not in prd_name):
            prd_name.append(i.name)
    
    brand=json.dumps(list(brand))
    brand_id=json.dumps(list(brand_id))
    cat_data=json.dumps(list(cat))
    cat_id=json.dumps(list(cat_id_obj))
    prd_name=json.dumps(list(prd_name))

    if request.method =='POST' and request.POST['action']=='list':
        global id_brand
        global id_category
        id_brand=request.POST.getlist('brand[]')
        id_category=request.POST.getlist('cat[]')


    if request.method =='POST' and request.POST['action']=='send_var':
        nav=request.POST.get('alt')
        
        try:
            nav_id=Product.objects.get(product_group=nav)
        except:
            messages.success(request,"Sorry this Product group is currently unavailable")
            return redirect('')
        nav_id=Product.objects.get(product_group=nav)
        id_category.clear()
        id_brand.clear()
        nav_id="category"+str(nav_id)
        id_category.append(nav_id)


    object_list=Product.objects.filter(add_home=True).order_by("?")[:8]
    x = list(object_list)
    l = len(x)
    i=0
    while(l%4!=0):
        x.append(x[i])
        l=l+1
        i=i+1
    print(x)


    if request.method =='POST' and request.POST['action']=='location':
        loc=request.POST.get('loc')
        data=Product.objects.filter(Q(brand=loc) | Q(product_group=loc) | Q(name=loc))

        xx=serializers.serialize('json',list(data))
        x=serializers.serialize('json',x)
        context={
            'loc_data':xx,
            'queryset':x                   
            }
        
        return JsonResponse(context)

    context={'brand_data':brand,
             'brand_id':brand_id,
             'x':x,  
             'cat_data':cat_data,
             'cat_id':cat_id, 
             'prd_name':prd_name                    
             }
    return render(request,'index.html', context)
    
        
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
   
    product = Product.objects.filter().order_by("?")[:4]
    product1 = Product.objects.filter().order_by("?")[:8]
    context={"search_product":queryset,
             'brand_data':brand,
             'brand_id':brand_id,
             'cat_data':cat_data,
             'cat_id':cat_id,
             'product':product,
             'product1':product1
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
        

class SearchView(View):
    def get(self, *args ,**kwargs):
        category = self.request.GET.get("category")
        if category == "Kitchen Stoves":
            product = Product.objects.filter(product_group=category)
        if category == "Mixer Grinder":
            product = Product.objects.filter(product_group=category)
        if category == "Rice Cookers":
            product = Product.objects.filter(product_group=category)
        if category == "Food Processors":
            product = Product.objects.filter(product_group=category)
        if category == "Electric Mixers":
            product = Product.objects.filter(product_group=category)
        if category == "Juicers":
            product = Product.objects.filter(product_group=category)
        if category == "Blenders":
            product = Product.objects.filter(product_group=category)
        if category == "Water Heaters":
            product = Product.objects.filter(product_group=category)
        if category == "Water Filters":
            product = Product.objects.filter(product_group=category)
        if category == "Induction Cookers":
            product = Product.objects.filter(product_group=category)
        if category == "Exhaust Hoods":
            product = Product.objects.filter(product_group=category)
        if category == "Sandwich Makers":
            product = Product.objects.filter(product_group=category)
        if category == "Toaster":
            product = Product.objects.filter(product_group=category)
        if category == "Deep Fryers":
            product = Product.objects.filter(product_group=category)
        if category == "Dough Blenders":
            product = Product.objects.filter(product_group=category)
        if category == "Coffee Makers":
            product = Product.objects.filter(product_group=category)
        if category == "Electric Iron":
            product = Product.objects.filter(product_group=category)
        if category == "Vaccum Cleaner":
            product = Product.objects.filter(product_group=category)
        if category == "Air Purifiers":
            product = Product.objects.filter(product_group=category)
        if category == "Hair Dryer":
            product = Product.objects.filter(product_group=category)
        if category == "Trimmers & Savers":
            product = Product.objects.filter(product_group=category)
        context = {'product':product
        }
        if len(product)<1:
            messages.warning(self.request, product," not found")
            return redirect("/")
        if len(product)>1:
            length = len(product)
            # messages.success(self.request, length, product " found")
        return render(self.request, 'category.html', context)
            