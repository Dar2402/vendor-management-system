from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Vendor
from .utils import calculate_vendor_performance_metrics
from purchase_orders.models import *

@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, **kwargs):
    calculate_vendor_performance_metrics(instance.vendor)