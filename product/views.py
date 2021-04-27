from django.shortcuts import render, get_object_or_404
from . models import Product
from dashboard.models import SellerCompany, BusinessProfile
from django.views.generic import ListView
from django.contrib.auth.models import User


################################## this is for displaying the home page ################################## 
class HomeView(ListView):
    model = Product
    template_name = "index.html"

    # def get_queryset(self):
        # return Product.objects.filter(add_home=True)
    #     # return Product.objects.raw('SELECT  DISTINCT user_id from product_product WHERE add_home=True')
    #     return Product.objects.order_by('user_id').values_list('user_id', flat=True).distinct()
    
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
        context['business_profile'] = BusinessProfile.objects.filter(user=user)
        return context
        
from django.http import HttpResponse
import json

    #     return redirect('http://127.0.0.1:8000/ecommerce/sell/')
    # return render(request,'ecommerce/sell.html')
def index(request):
    print("YEs")
    brand=Product.objects.values_list('brand', flat=True)
    brand=list(brand)
    return render(request,'index.html',{'brand_data':json.dumps(brand)})

    if request.is_ajax():
       brand=request.POST.getlist('brand[]')
       print(brand)
       return HttpResponse('success') 
    return render(request,'index.html',{'brand_data':json.dumps(brand)})
