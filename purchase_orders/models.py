from django.db import models
from vendors.models import Vendor
from django.db.models.signals import post_save
from django.dispatch import receiver
from vendors.utils import *

# Create your models here.


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.po_number}"

@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, **kwargs):
    if instance.acknowledgment_date:
        vendor = instance.vendor
        calculate_vendor_performance_metrics(vendor)