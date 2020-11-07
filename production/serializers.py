from rest_framework import serializers
from .models import District,Production,Crop

class productionSerializer(serializers.ModelSerializer):
  # crop = serializers.StringRelatedField(many = False)
  class Meta:
    model = Production
    fields = '__all__'
  
class districtSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields = '__all__'
  
class cropSerializer(serializers.ModelSerializer):
  class Meta:
    model = Crop
    fields = '__all__'