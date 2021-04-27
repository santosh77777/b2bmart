from django.contrib import admin
from .models import SellerProfile, SellerBank, SellerStatutory, BusinessProfile, SellerCompany

admin.site.register(SellerProfile)
admin.site.register(SellerBank)
admin.site.register(SellerStatutory)
admin.site.register(BusinessProfile)
admin.site.register(SellerCompany)

