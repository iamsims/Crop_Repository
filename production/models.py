from django.db import models
import datetime

def year_choices():
    years = [(r,(r+1)%100) for r in range(1984, datetime.date.today().year+1)]
    actual_value = [int(str(a).zfill(2) + str(b).zfill(2)) for a,b in years] 
    readable_form =['/'.join([str(a).zfill(2),str(b).zfill(2)]) for a,b in years] 
    return list(zip(actual_value, readable_form))

class Crop(models.Model):
    name = models.CharField(max_length=20,  unique=True)
    crop_type = models.CharField(max_length=15)
    image = models.ImageField(upload_to = 'images/', null = True)

    def __str__(self):
        return self.name
    
class District(models.Model):
    name = models.CharField(max_length=20, unique=True)
    area = models.FloatField()
    pradesh_no = models.IntegerField()

    def __str__(self):
        return self.name

class Production(models.Model):
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    year = models.IntegerField( choices=year_choices())
    amount =models.FloatField()
    harvest_area =models.FloatField(null=True)
    ph_value = models.FloatField(null=True)
    climate = models.FloatField(null=True)
    
    def __str__(self):
        return self.crop.name + " " + self.district.name + " " + str(self.year)
