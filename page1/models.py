from django.db import models
import geocoder

# Create your models here.

class Plot(models.Model):
    owner_name = models.CharField(max_length=20,default='')
    owner_profession=models.CharField(max_length=15,default='')
    contact = models.CharField(max_length=11,default='')
    district = models.CharField(max_length=15,default='')
    address = models.CharField(max_length=500,null=True)
    selling_date =models.DateField(default='XXXX-XX-XX')
    plot_desc = models.CharField(max_length=150,default='')
    price = models.IntegerField(default=0)


    def __str__(self) :
        return self.owner_name



