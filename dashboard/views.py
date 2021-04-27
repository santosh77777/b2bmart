from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.views.generic.detail import DetailView
from accounts.models import Account
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.contrib import messages
from product.models import Product
from .models import SellerProfile, Account, SellerStatutory, SellerBank, BusinessProfile
from accounts.views import is_seller, is_buyer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *
from product.forms import ProductForm
from product.models import Product,EshopeForm


class SellerDashboardView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/dashboard.html')

class SellerContactProfileView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def post(self,request, *args, **kwargs):
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        promoter_first_name =request.POST['promoter_first_name']
        promoter_last_name =request.POST['promoter_last_name']
        company =request.POST['company']
        designation =request.POST['designation']
        address_building =request.POST['address_building']
        address_area =request.POST['address_area']
        landmark =request.POST['landmark']
        locality =request.POST['locality']
        city =request.POST['city']
        state =request.POST['state']
        country =request.POST['country']
        pincode =request.POST['pincode']
        gstin =request.POST['gstin']
        company_website =request.POST['company_website']
        mobile =request.POST['mobile']
        alternative_mobile =request.POST['alternative_mobile']
        email =request.POST['email']
        alternative_email =request.POST['alternative_email']
        landline_no =request.POST['landline_no']
        alternative_landline_no =request.POST['alternative_landline_no']
        about_me =request.POST['about_me']
        user = User.objects.get(username=request.user.username)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        account = Account.objects.get(user=request.user)
        account.mobile = mobile
        account.state = state
        account.pincode = pincode
        account.company_name = company
        account.save()
        try:
            seller = SellerProfile.objects.filter(user=request.user)[0]
            if seller:
                seller.user = request.user
                seller.promoter_first_name = promoter_first_name
                seller.promoter_last_name = promoter_last_name
                seller.designation = designation
                seller.address_building = address_building
                seller.address_area = address_area
                seller.landmark = landmark
                seller.city = city
                seller.country = country
                seller.gstin = gstin
                seller.company_website = company_website
                seller.alternative_mobile = alternative_mobile
                seller.alternative_email = alternative_email
                seller.landline_no = landline_no
                seller.alternative_landline_no = alternative_landline_no
                seller.about_me = about_me
                seller.save()
                return redirect(".")
        except:
            seller = SellerProfile(user=request.user, promoter_first_name=promoter_first_name,
                promoter_last_name=promoter_last_name, designation=designation, address_building=address_building,
                address_area=address_area, 
                landmark=landmark, locality=locality, city=city,country=country,
                gstin=gstin, company_website=company_website, alternative_mobile=alternative_mobile,
                alternative_email=alternative_email, landline_no=landline_no, 
                alternative_landline_no=alternative_landline_no, about_me=about_me)
            seller.save()
            return redirect(".")

    def get(self,request, *args, **kwargs):

        account = Account.objects.get(user=request.user)
        try:
            seller = SellerProfile.objects.get(user=request.user)
            context = {'account': account,
                    'seller': seller
                    }
        except:
            context = {'account': account
                    }
        return render(request, 'dashboard/seller/contact_profile.html', context)

class SellerStatutoryView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller
    def post(self,request, *args, **kwargs):
            try:
                statutory = SellerStatutory.objects.get(user=request.user)
                if statutory:
                    statutory.gst_no = request.POST['gst_no']
                    statutory.pan_no = request.POST['pan_no']
                    statutory.tan_no = request.POST['tan_no']
                    statutory.cin_no = request.POST['cin_no']
                    statutory.dgft_ie_code = request.POST['dgft_ie_code']
                    statutory.company_registration_no = request.POST['company_registration_no']
                    statutory.save()
            except:
                gst_no = request.POST['gst_no']
                pan_no = request.POST['pan_no']
                tan_no = request.POST['tan_no']
                cin_no = request.POST['cin_no']
                dgft_ie_code = request.POST['dgft_ie_code']
                company_registration_no = request.POST['company_registration_no']
                statutory = SellerStatutory(user=request.user, gst_no=gst_no,
                            pan_no=pan_no,tan_no=tan_no, cin_no=cin_no,
                            dgft_ie_code=dgft_ie_code,company_registration_no=company_registration_no)
                statutory.save()
                return redirect(".")
                
            return redirect(".")  

    def get(self,request, *args, **kwargs):
        try:
            statutory = SellerStatutory.objects.get(user=request.user)
            context = { 'statutory':statutory}
        except:
            context=None
        return render(request, 'dashboard/seller/statutory.html', context)


@login_required
def SellerBusinessProfileView(request):
    #seller = BusinessProfile.objects.get(user=request.user)
    seller = request.user.businessprofile
    form = BusinessProfileForm(instance= seller)

    if request.method == 'POST':
        form = BusinessProfileForm(request.POST, request.FILES, instance=seller)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully')


    context = {'form':form, 'seller': seller }
    return render(request, 'dashboard/seller/business_profile.html', context)

class SellerBankView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)
    
    def post(self,request, *args, **kwargs):
        form = SellerBankForm(request.POST)
        if form.is_valid:
            try:
                dilip = form.save(commit=False)
                dilip.user = request.user
                dilip.save()
                return redirect(".")
            except:
                seller_bank = SellerBank.objects.get(user=request.user)
                seller_bank.bank_name = form.cleaned_data['bank_name']
                seller_bank.account_no = form.cleaned_data['account_no']
                seller_bank.bank_account_name = form.cleaned_data['bank_account_name']
                seller_bank.ifsc_code = form.cleaned_data['ifsc_code']
                seller_bank.account_type = form.cleaned_data['account_type']

                seller_bank.alternative_bank_name = form.cleaned_data['alternative_bank_name']
                seller_bank.alternative_account_no = form.cleaned_data['alternative_account_no']
                seller_bank.alternative_bank_account_name = form.cleaned_data['alternative_bank_account_name']
                seller_bank.alternative_bank_ifsc_code = form.cleaned_data['alternative_bank_ifsc_code']
                seller_bank.alternative_bank_account_type = form.cleaned_data['alternative_bank_account_type']
                seller_bank.save()
                return redirect(".")                    

    def get(self,request, *args, **kwargs):
        try:
            seller_bank = SellerBank.objects.get(user=request.user)
            context= {'seller_bank':seller_bank}
        except:
            context = None
        return render(request, 'dashboard/seller/bank_details.html', context)

class SellerAddProductView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def post(self,request, *args, **kwargs):
        if request.method == "POST":  
            user = request.user                  
            name=request.POST.get('Product_name')          
            price= request.POST.get('price','')   
            min_order_quantity= request.POST.get('min_order_qty','') 
            unity_type= request.POST.get('unity_type','')
            product_group= request.POST.get('product_group','')
            description= request.POST.get('desc','')
            packing_details= request.POST.get('packing_details','')
            product_video_url= request.POST.get('product_video_url','')
            capacity= request.POST.get('capacity','')     
            material= request.POST.get('material','')            
            brand= request.POST.get('brand','')             
            color= request.POST.get('color','')      
            size= request.POST.get('size','')                       
            model_no= request.POST.get('model_no','')      
            power= request.POST.get('power','')      
            warranty= request.POST.get('warranty','')      
            rating= request.POST.get('rating','')      
            neck_size= request.POST.get('neck_size','')
            closure_type= request.POST.get('closure_type','')      
            product_code= request.POST.get('product_code','')      
            is_available= request.POST.get('is_available','')  
            video_url= request.POST.get('video_url','')        

            image1= request.FILES.get('image1','')
            image2 =request.FILES.get('image2','')
            image3 =request.FILES.get('image2','') 
            product = Product(user=user,name=name,price=price,min_order_quantity=min_order_quantity,unity_type=unity_type,product_group=product_group,
            description=description,capacity=capacity,material=material,color=color,brand=brand,warranty=warranty,
            size=size,model_no=model_no,power=power,rating=rating,neck_size=neck_size,closure_type=closure_type,
            product_code=product_code,is_available=is_available,image1=image1,image2=image2,image3=image3,packing_details=packing_details,video_url=video_url)
            product.save()
            messages.success(request,"Congratulations your details are successfully saved!")
            return redirect(".")

   

    def get(self,request, *args, **kwargs):
        form = ProductForm()
        return render(request, 'dashboard/seller/add_product.html',{'form':form})

@login_required
def SellerManageProductView(request):
        seller = User.objects.get(id=request.user.pk)
        product = Product.objects.all()
        products = product.filter(user=request.user)
        #product_count = products.count()
        context = {'products':products, 'seller':seller}
        return render(request, 'dashboard/seller/manage_product.html', context)


@login_required
def SellerBulkPriceUpdateView(request, pk):
        ProductFormSet = inlineformset_factory(User, Product, fields=('name', 'price'), extra=0,  can_delete = False )
        seller = User.objects.get(id=pk)
        formset = ProductFormSet(instance=seller)
        if request.method == 'POST':
            formset = ProductFormSet(request.POST, instance=seller)
            if formset.is_valid():
                formset.save()
                return redirect('dashboard:seller_manage_product')

        context = {'form':formset}
        return render(request, 'dashboard/seller/bulk_price_update.html', context)


"""
@login_required
def SellerBulkPriceUpdateView(request, pk):
        product = Product.objects.get(id=pk)
        form = SellerManageProductViewForm(instance=product)
        if request.method == 'POST':
            form = SellerManageProductViewForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your price updated successfully')
                return redirect('dashboard:seller_manage_product')


        context = {'form':form, 'product': product }
        return render(request, 'dashboard/seller/bulk_price_update.html', context)
"""
 
@login_required
def sellerDeleteProduct(request, pk):
    context ={} 
    # fetch the object related to passed id 
    obj = get_object_or_404(Product, id = pk) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to
        return redirect('dashboard:seller_manage_product')
  
    return render(request, "dashboard/seller/delete.html", context) 


class SellerReArrangeProductView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Product
    template_name = "dashboard/seller/rearrange_product.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def test_func(self):
        return is_seller(self.request.user)

class SellerCategoryReportView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/seller_category_report.html')

class SellerAnalyticView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/analytics.html')

class SellerBusinessOutlookView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/businessoutlook.html')

class SellerFinancecView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/finance.html')

class SellerHistoryView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/history.html')

class SellerPhotoDocumentView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/document.html')

class SellerMembershipView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/membership.html')

class SellerMyEnquiryView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/myenquiry.html')

class SellerSettingsView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/seller/settings.html')
    
class SellerPaidServiceView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        return render(request, 'dashboard/certificate.html')

class SellerCompanyView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return is_seller(self.request.user)
    model = Product
    template_name = 'dashboard/company.html'

    def get_queryset(self):
        return Product.objects.filter(arrange=True)

    def get_context_data(self,**kwargs):
        context = super(SellerCompanyView,self).get_context_data(**kwargs)
        context['object_all_list'] = Product.objects.all()
        return context

class SellerProductDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):  
    model = Product
    template_name = 'dashboard/productdetail.html'

    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs.get("pk"))

    def post(self,request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            mobile = request.POST.get('phone','')
            nature_of_business = request.POST.get('business','')
            mesg = request.POST.get('msg','')
            send_copy = request.POST.get('sendcopy','')

            data = EshopeForm(name=name,email=email,mobile=mobile,nature_of_business=nature_of_business,messages=mesg,send_copy=send_copy)
            data.save()
            messages.success(request,"Congratulations your details are successfully saved!")
            return redirect(".")

    def test_func(self):
        return is_seller(self.request.user)

    # def get(self,request, *args, **kwargs):
    #     return render(request, 'dashboard/productdetail.html')

class SellerArangeProductView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self,request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        product.arrange = True
        product.save()
        return redirect('/dashboard/seller/rearrange-product/')
    def test_func(self):
        return is_seller(self.request.user)

class SellerUnArangeProductView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        product.arrange = False
        product.save()
        return redirect('/dashboard/seller/rearrange-product/')

class SellerAddHomeView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self,request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        product.add_home = True
        product.save()
        return redirect('/dashboard/seller/rearrange-product/')
    def test_func(self):
        return is_seller(self.request.user)

class SellerRemoveHomeView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return is_seller(self.request.user)

    def get(self,request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        product.add_home = False
        product.save()
        return redirect('/dashboard/seller/rearrange-product/')


from .models import SellerCompany
@login_required
def SellersCompanyView(request):
    if request.method == 'POST':
        logo = request.FILES['logo']
        banner_image = request.FILES['banner_image']
        about_seller = request.POST['about_seller']
        branded_video = request.POST['branded_video']
        catalogue = request.FILES['catalogue']
        no_of_employees = request.POST['no_of_employees']
        legal_status_of_firm = request.POST['legal_status_of_firm']
        try:
            seller_company = SellerCompany.objects.get(user=request.user)
            seller_company.logo = logo
            seller_company.banner_image = banner_image
            seller_company.about_seller = about_seller
            seller_company.branded_video = branded_video
            seller_company.catalogue = catalogue
            seller_company.no_of_employees = no_of_employees
            seller_company.legal_status_of_firm = legal_status_of_firm
            seller_company.save()
        except:
            seller_company = SellerCompany(user=request.user, logo=logo, banner_image=banner_image, about_seller=about_seller, 
                            branded_video=branded_video, catalogue=catalogue, no_of_employees=no_of_employees,
                            legal_status_of_firm=legal_status_of_firm) 
            seller_company.save()
        messages.success(request, 'Your profile was updated successfully')
    try:
        seller_company = SellerCompany.objects.get(user=request.user)
        context = {'seller_company':seller_company}
    except:
        context=None
    return render(request, 'dashboard/seller/seller_company.html', context)