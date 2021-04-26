from django.shortcuts import render
from . models import Product
from django.http import HttpResponse
import json

    #     return redirect('http://127.0.0.1:8000/ecommerce/sell/')
    # return render(request,'ecommerce/sell.html')
id_brand=[]
def index(request):
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
    return render(request,'index.html',{'brand_data':brand,'brand_id':brand_id})

def category(request):
    print("category")
    print(id_brand)
    return render(request,'category.html')