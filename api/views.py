from django.shortcuts import render

from rest_framework import viewsets

from .serializers import productionSerializer,districtSerializer,cropSerializer
from production.models import Production,Crop,District
# Create your views here.
class ProductionView(viewsets.ModelViewSet):
    queryset = Production.objects.all().order_by('year')
    serializer_class = productionSerializer
  
class DistrictView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = districtSerializer

class CropView(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = cropSerializer