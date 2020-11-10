from django.shortcuts import render
from django.http import HttpResponse 
from .models import Crop,District,Production
from .serializers import cropSerializer,districtSerializer,productionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.mixins import ListModelMixin
from django.db import connection
#from  django.core import serializers
import json

# Create your views here.

class CropView(APIView):

    def get(self,request):
        crops = Crop.objects.all()
        serializer = cropSerializer(crops,many = True)
        return Response(serializer.data)

    def post(self, request):
        crop = request.data
        # print('here')
        # Create crop from the above data
        serializer = cropSerializer(data=crop)
        if serializer.is_valid(raise_exception=True):
            crop_saved = serializer.save()
            print(crop_saved)
        return Response(serializer.data)

    def post(self, request):
        crop = request.data
        # print('here')
        # Create crop from the above data
        serializer = cropSerializer(data=crop)
        if serializer.is_valid(raise_exception=True):
            crop_saved = serializer.save()
            print(crop_saved)
        return Response(serializer.data)

    # def get(self, request, pk):
    #     crop = Crop.objects.get(pk=pk)
    #     serializer = cropSerializer(crop)
    #     return Response(serializer.data)

    def put(self, request, pk):
        saved_crop = Crop.objects.get(pk=pk)
        data = request.data
        serializer = cropSerializer(saved_crop,data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self,request,pk):
        crop = Crop.objects.get(pk=pk)
        here = crop
        crop.delete()
        serializer = cropSerializer(here)
        return Response(serializer.data)

class DistrictView(APIView):

    def get(self,request):
        districts = District.objects.all()
        serializer = districtSerializer(districts,many = True)
        return Response(serializer.data)

class ProductionView(APIView):

    def get(self,request):
        cursor = connection.cursor()
        cursor.execute("SELECT p.year, p.amount, p.harvest_area, c.name, d.name FROM  production_district d INNER JOIN production_production p ON d.id=p.district_id INNER JOIN production_crop c ON c.id=p.crop_id")
        rows = cursor.fetchall()
        keys = ('year','amount','harvest_area','crop_name','district_name')
        result =[]
        for row in rows:
            result.append(dict(zip(keys,row)))
        json_data = json.dumps(result)
        
        return HttpResponse(json.dumps(result),content_type="application/json")
        
    def post(self,request):
        distname = request.data["district"]
        cropname = request.data["crop"]
        cursor = connection.cursor()
        print("SELECT id FROM production_crop p WHERE p.name='{0}'".format(cropname))
        crop_id = cursor.execute("SELECT id FROM production_crop p WHERE p.name='{0}'".format(cropname))
        district_id = cursor.execute("SELECT id FROM production_district p WHERE p.name='{0}'".format(distname))
        print(crop_id)
        print(district_id)
        # crop_id = Crop.objects.get()
        data = {
            "crop_id" : crop_id,
            "district_id" : district_id,
            "year" : request.data["year"],
            "harvest_area": request.data["harvest_area"],
            "amount":request.data["amount"]
        }
        serializer = productionSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            production_saved = serializer.save()
            print(production_saved)
        return Response(serializer.data)
