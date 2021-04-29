from django.contrib import admin
from .models import SellerProfile, SellerBank, SellerStatutory, BusinessProfile, SellerCompany, ShareDetail

admin.site.register(SellerProfile)
admin.site.register(SellerBank)
admin.site.register(SellerStatutory)
admin.site.register(BusinessProfile)
admin.site.register(SellerCompany)
admin.site.register(ShareDetail)

