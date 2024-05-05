from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import *
from django.shortcuts import get_object_or_404

# Create your views here.

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

@api_view(['GET'])
def vendor_performance(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    calculate_vendor_performance_metrics(vendor)
    serializer = VendorSerializer(vendor)
    return Response(serializer.data)
