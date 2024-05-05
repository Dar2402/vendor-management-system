from django.db import models
from datetime import timedelta

def calculate_vendor_performance_metrics(vendor):
    completed_pos = vendor.purchaseorder_set.filter(status='completed')
    total_completed_pos = completed_pos.count()

    if total_completed_pos > 0:
        on_time_delivery_rate = completed_pos.filter(delivery_date__lte=models.F('delivery_date')).count() / total_completed_pos
        quality_rating_avg = completed_pos.aggregate(avg_quality_rating=models.Avg('quality_rating'))['avg_quality_rating']
        average_response_time_seconds = completed_pos.aggregate(avg_response_time=models.Avg(models.F('acknowledgment_date') - models.F('issue_date')))['avg_response_time'].total_seconds()
        average_response_time_hours = average_response_time_seconds / 3600
        fulfillment_rate = completed_pos.filter(status='completed').count() / vendor.purchaseorder_set.count()
    else:
        on_time_delivery_rate = 0
        quality_rating_avg = 0
        average_response_time_hours = 0
        fulfillment_rate = 0

    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_avg
    vendor.average_response_time = average_response_time_hours
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()
