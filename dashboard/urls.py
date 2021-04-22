from django.urls import path
from . import views
app_name = "dashboard"

urlpatterns = [
    path('seller-dashboard/',views.SellerDashboardView.as_view(), name="seller_dashboard"),
    path('seller/contact-profile/',views.SellerContactProfileView.as_view(), name="seller_contact_profile"),
    path('seller/business-profile/',views.SellerBusinessProfileView, name="seller_business_profile"),
    path('seller/statutory/',views.SellerStatutoryView.as_view(), name="seller_statutory"),
    path('seller/bank/',views.SellerBankView.as_view(), name="seller_bank"),
    
    
    
    path('seller/add-product/',views.SellerAddProductView.as_view(), name="seller_add_product"),
]



