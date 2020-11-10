from rest_framework import serializers
from django.db import models
from .models import District,Production,Crop
from django.db import connection

# def sql(self):
#   with connection.cursor()as cursor:
#     cursor.execute(" select p.year, p.amount, p.harvest_area, c.name, d.name
#       from  district d
#       inner production p 
#       inner join  crops c")

class districtSerializer(serializers.ModelSerializer):
  # districts = productionSerializer(many=True)
  class Meta:
    model = District
    fields = "__all__"
  
class cropSerializer(serializers.ModelSerializer):
  # crops = productionSerializer(many = True)
  class Meta:
    model = Crop
    #fields = ['name','crops']
    fields = "__all__"


class productionSerializer(models.Model):

  crop_name = models.CharField(max_length=20)
  district_name = models.CharField(max_length=20)
  year = models.IntegerField()
  amount =models.FloatField()
  harvest_area =models.FloatField()

