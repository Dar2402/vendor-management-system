from django.utils import timezone
from datetime import timedelta
from django.db.models import Avg
from .models import HistoricalPerformance
from purchase_orders.models import PurchaseOrder

# def update_historical_performance_metrics(vendor):
#     completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
#     total_completed_pos = completed_pos.count()
#     on_time_delivery_count = completed_pos.filter(delivery_date__lte=timezone.now()).count()
#     on_time_delivery_rate = on_time_delivery_count / total_completed_pos if total_completed_pos > 0 else 0

#     quality_rating_avg = completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

#     response_times = completed_pos.exclude(acknowledgment_date=None).annotate(response_time=timezone.F('acknowledgment_date') - timezone.F('issue_date')).aggregate(Avg('response_time'))['response_time__avg']
#     average_response_time_hours = response_times.total_seconds() / 3600 if response_times else 0

#     fulfilled_pos_count = completed_pos.filter(status='completed').count()
#     fulfillment_rate = fulfilled_pos_count / total_completed_pos if total_completed_pos > 0 else 0

#     historical_performance, created = HistoricalPerformance.objects.get_or_create(vendor=vendor)
#     historical_performance.on_time_delivery_rate = on_time_delivery_rate
#     historical_performance.quality_rating_avg = quality_rating_avg
#     historical_performance.average_response_time = average_response_time_hours
#     historical_performance.fulfillment_rate = fulfillment_rate
#     historical_performance.save()

def update_historical_performance_metrics(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    total_completed_pos = completed_pos.count()
    on_time_delivery_count = completed_pos.filter(delivery_date__lte=timezone.now()).count()
    on_time_delivery_rate = on_time_delivery_count / total_completed_pos if total_completed_pos > 0 else 0

    quality_rating_avg = completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    total_response_time_seconds = 0
    response_count = 0
    for po in completed_pos.exclude(acknowledgment_date=None):
        response_time = po.acknowledgment_date - po.issue_date
        total_response_time_seconds += response_time.total_seconds()
        response_count += 1
    average_response_time_hours = total_response_time_seconds / 3600 if response_count > 0 else 0

    fulfilled_pos_count = completed_pos.filter(status='completed').count()
    fulfillment_rate = fulfilled_pos_count / total_completed_pos if total_completed_pos > 0 else 0

    print('average_response_time_hours:', average_response_time_hours, type(average_response_time_hours))

    historical_performance, created = HistoricalPerformance.objects.get_or_create(vendor=vendor)
    historical_performance.on_time_delivery_rate = on_time_delivery_rate
    historical_performance.quality_rating_avg = quality_rating_avg
    historical_performance.average_response_time = float(str(average_response_time_hours))
    historical_performance.fulfillment_rate = fulfillment_rate
    historical_performance.save()