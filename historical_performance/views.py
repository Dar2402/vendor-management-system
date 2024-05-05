from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer
from vendors.models import Vendor
from .utils import update_historical_performance_metrics

# Create your views here.

class HistoricalPerformanceListCreate(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class HistoricalPerformanceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

@api_view(['GET'])
def vendor_historical_performance(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    update_historical_performance_metrics(vendor)
    queryset = HistoricalPerformance.objects.filter(vendor=vendor)
    serializer = HistoricalPerformanceSerializer(queryset, many=True)
    return Response(serializer.data)