from django.contrib import admin
from .models import HistoricalPerformance

# Register your models here.

@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    list_filter = ('on_time_delivery_rate', 'quality_rating_avg', 'fulfillment_rate')

