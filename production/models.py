from django.db import models
import datetime

def year_choices():
    return [(r,r+1) for r in range(1984, datetime.date.today().year+1)]

class Crop(models.Model):
    name = models.CharField(max_length=15)
    crop_type = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class District(models.Model):
    name = models.CharField(max_length=15)
    region = models.CharField(max_length=15)
    pradesh_no = models.IntegerField()

    def __str__(self):
        return self.name

class Production(models.Model):
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    year = models.IntegerField( choices=year_choices())







    