from django.urls import path,include
from .views import CropView,DistrictView,ProductionView

app_name = "production"

urlpatterns = [
    path('crop/', CropView.as_view()),
    path('crop/<int:pk>', CropView.as_view()),
    path('district/', DistrictView.as_view()),
    path('production/',ProductionView.as_view()),
    path('production/<int:pk>',ProductionView.as_view()),
]