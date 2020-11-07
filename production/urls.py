from django.urls import path,include
from .views import CropView

app_name = "production"

urlpatterns = [
    path('crop/', CropView.as_view()),
    # path('about/', views.about, name='production-about'),
    path('crop/<int:pk>', CropView.as_view())
]