from django.contrib import admin
from .models import SellerProfile, SellerBank, SellerStatutory

admin.site.register(SellerProfile)
admin.site.register(SellerBank)
admin.site.register(SellerStatutory)
