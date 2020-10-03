from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='production-home'),
    path('about/', views.about, name='production-about'),

]