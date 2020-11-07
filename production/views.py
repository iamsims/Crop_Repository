from django.shortcuts import render
from django.http import HttpResponse 
from .models import Crop
from .serializers import cropSerializer
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.mixins import ListModelMixin

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
