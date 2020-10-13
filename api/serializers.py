from rest_framework import serializers
from production.models import District,Production,Crop

class productionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Production
    fields = ('crops','district','year')
  
class districtSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = District
    fields = ('name','area','pradesh_no')
  
class cropSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Crop
    fields = ('name','crop_type')