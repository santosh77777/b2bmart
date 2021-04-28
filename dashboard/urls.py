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
    path('seller/manage-product/',views.SellerManageProductView, name="seller_manage_product"),
    path('seller/rearrange-product/',views.SellerReArrangeProductView.as_view(), name="seller_rearrange_product"),
    path('seller/bulk-price-update/<str:pk>',views.SellerBulkPriceUpdateView, name="seller_bulk_price_update"),
    path('seller/single-product-update/<str:pk>', views.SellerSingleProductUpdateView, name="seller_single_product_update"),
    path('<int:pk>/delete_product/', views.sellerDeleteProduct, name="seller_delete_product"),
    path('seller/category-report/',views.SellerCategoryReportView.as_view(), name="seller_category_report"),
    path('seller/analytics/',views.SellerAnalyticView.as_view(), name="seller_analytics"),
    

    path('seller/business-outlook/',views.SellerBusinessOutlookView.as_view(), name="seller_business_outlook"),
    path('seller/finance/',views.SellerFinancecView.as_view(), name="seller_finance"),
    path('seller/history/',views.SellerHistoryView.as_view(), name="seller_history"),
    path('seller/document/',views.SellerPhotoDocumentView.as_view(), name="seller_document"),
    path('seller/membership/',views.SellerMembershipView.as_view(), name="seller_membership"),
    path('seller/my-enquiry/',views.SellerMyEnquiryView.as_view(), name="seller_my_enquiry"),
    path('seller/settings/',views.SellerSettingsView.as_view(), name="seller_settings"),
    path('seller/paid-service/',views.SellerPaidServiceView.as_view(), name="seller_paid_service"),

    path('seller/company/<str:user>/',views.SellerCompanyView.as_view(), name="seller_company"),
    path('seller/product-detail/<int:pk>/',views.SellerProductDetailView.as_view(), name="seller_product_detail"),

    path('seller/arrange-product/<int:pk>/',views.SellerArangeProductView.as_view(), name="seller_arrange_product"),
    path('seller/unarrange-product/<int:pk>/',views.SellerUnArangeProductView.as_view(), name="seller_unarrange_product"),

    path('seller/add-home-product/<int:pk>/',views.SellerAddHomeView.as_view(), name="seller_add_home_product"),
    path('seller/remove-home-product/<int:pk>/',views.SellerRemoveHomeView.as_view(), name="seller_remove_home_product"),

    path('seller/companey-add/',views.SellersCompanyView, name="seller_company_add"),


    ####################################### Buyer #####################################
    path('buyer-dashboard/',views.BuyerDashboardView.as_view(), name="buyer_dashboard"),
    path('buyer-profile/',views.BuyerProfileView.as_view(), name="buyer_profile"),
    path('buyer-order/',views.BuyerOrderView.as_view(), name="buyer_order"),
    path('buyer-message/',views.BuyerMessageView.as_view(), name="buyer_message"),
    path('buyer-offer-request-detail/',views.BuyerOfferRequestDetailsView.as_view(), name="buyer_offer_request_detail"),
    path('buyer-enquiry/',views.BuyerEnquiryView.as_view(), name="buyer_enquiry"),
    path('buyer-recent-activity/',views.BuyerRecentActivityView.as_view(), name="buyer_recent_activity"),
    path('buyer-favourite/',views.BuyerFavouriteView.as_view(), name="buyer_favourite"),
    path('buyer-downloads/',views.BuyerDownloadsView.as_view(), name="buyer_downloads"),
    path('buyer-share/',views.BuyerShareView.as_view(), name="buyer_share"),

]



