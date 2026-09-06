from django.db import models
from accounts.models import (Clients,decrementRequest)

# Create your models here.




class Packages(models.Model):
    id=models.AutoField(primary_key=True)
    PACKAGE_TYPE= {
        "N": "Normal",
        "ES": "Especial",
    }
    type=models.CharField(max_length=3,choices=PACKAGE_TYPE,blank=False)
    name= models.CharField(max_length=50,blank=False)
    created_date=models.DateField(auto_now_add=True)
    end_date=models.DateField(blank=True)
    is_active=models.BooleanField(default=True)
    price=models.BigIntegerField()
    duration=models.IntegerField()
    trafic_quota=models.IntegerField()
    desc=models.TextField(max_length=255,blank=True)
    




class discount(models.Model):
    id=models.AutoField(primary_key=True)
    code=models.CharField(max_length=25,unique=True)
    discount=models.DecimalField(max_digits=4,decimal_places=2)
    created_date=models.DateField(auto_now_add=True)
    end_date=models.DateField()
    packages=models.ManyToOneRel(Packages,related_name='packages',on_delete=models.SET_NULL)
    


class myPackages(models.Model):
    client = models.ForeignKey(
        Clients, verbose_name="mypackages", on_delete=models.RESTRICT)
    PACKAGE_TYPE = {
        "N": "Normal",
        "ES": "Especial",
    }
    type = models.CharField(max_length=3, choices=PACKAGE_TYPE, blank=False)
    startDate = models.DateField(auto_now_add=True)
    endDate = models.DateField()
    trafic_quota = models.IntegerField()
    remmaining_quota = models.IntegerField()
    active = models.BooleanField(default=True)
    statment = models.OneToOneField(decrementRequest, on_delete=models.CASCADE)