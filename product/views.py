from django.shortcuts import render
from . models import Product
import json

    #     return redirect('http://127.0.0.1:8000/ecommerce/sell/')
    # return render(request,'ecommerce/sell.html')
def index(request):
    brand=Product.objects.values_list('brand', flat=True)
    brand=list(brand)
    return render(request,'index.html',{'brand_data':json.dumps(brand)})