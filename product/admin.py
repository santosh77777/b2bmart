from django.contrib import admin
from .models import *

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Address, AddressAdmin)


