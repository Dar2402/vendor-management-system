from django.contrib import admin
from .models import PurchaseOrder

# Register your models here.

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date')
    list_filter = ('status', 'quality_rating')