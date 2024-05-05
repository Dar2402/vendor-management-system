from django.shortcuts import render
from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import *
from django.utils import timezone

# Create your views here.

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


@api_view(['POST'])
def acknowledge_purchase_order(request, pk):
    po = get_object_or_404(PurchaseOrder, pk=pk)
    po.acknowledgment_date = timezone.now()
    po.save()
    return Response({'message': 'Purchase order acknowledged successfully.'})