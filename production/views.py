from django.shortcuts import render
from django.http import HttpResponse 
from .models import Production

def home(request):
    context ={
        'posts' : Production.objects.all(),
    }
    return render(request, 'production/home.html', context)
# Create your views here.

def about (request):
    return render(request, 'production/about.html')

