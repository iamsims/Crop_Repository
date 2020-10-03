from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    context ={
        'posts' : [{'name': 'simran', 'age':21, 'place':"Pokhara"}],
    }
    return render(request, 'production/home.html', context)
# Create your views here.

def about (request):
    return render(request, 'production/about.html')
