from django.contrib import admin
from .models import District, Crop, Production

# Register your models here.
admin.site.register(District)
admin.site.register(Crop)
admin.site.register(Production)
