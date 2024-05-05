from django.contrib import admin
from .models import Vendor

# Register your models here.

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_details', 'address', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    list_filter = ('on_time_delivery_rate', 'quality_rating_avg', 'fulfillment_rate')
