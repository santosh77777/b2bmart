from django.shortcuts import render
from . models import Product
from django.http import HttpResponse
import json

    #     return redirect('http://127.0.0.1:8000/ecommerce/sell/')
    # return render(request,'ecommerce/sell.html')
def index(request):
    print("YEs")
    brand=Product.objects.values_list('brand', flat=True)
    brand=list(brand)
    if request.is_ajax():
       brand=request.POST.getlist('brand[]')
       print(brand)
       return HttpResponse('success') 
    return render(request,'index.html',{'brand_data':json.dumps(brand)})