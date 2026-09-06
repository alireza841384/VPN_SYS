from django.db import models
from accounts.models import Clients
from admin.models import admins

# Create your models here.

class localIp(models.models):
    ip=models.CharField(max_length=18)
    is_reserved=models.BooleanField(default=False)
    lastReserved=models.DateField(auto_now=True)



# class fireWallRules(models.model):
#     pass






class Session(models.model):
    client=models.ForeignKey(Clients,verbose_name='clientSession',on_delete=models.SET_NULL)
    ip=models.CharField(max_length=18)
    port=models.IntegerField()
    assignedIp=models.ForeignKey(localIp,on_delete=models.CASCADE)
    startDate=models.DateField(auto_now_add=True)
    endDate=models.DateField(blank=True)
    download=models.BigIntegerField(default=0)
    upload=models.BigIntegerField(default=0)
    choices=['active','disconnected','blocked']
    status=models.TextField(choices=choices)



class kickRequests(models.model):
    admin=models.ForeignKey(admins,verbose_name='kickRequest',on_delete=models.SET_NULL)
    session=models.OneToOneField(Session,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    desc=models.TextField(max_length=255)




class traficLogs(models.Model):
    session=models.ForeignKey(Session,verbose_name="trafic_logs",on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    toIp=models.CharField(max_length=18)
    toPort=models.IntegerField(blank=True)
    protocol=models.CharField(max_length=25)
    url=models.CharField(max_length=50,blank=True)
    method=models.CharField(max_length=15,blank=True)
    userAgent=models.CharField(max_length=25,blank=True)
    host=models.CharField(max_length=70)
    refered=models.CharField(max_length=100)
    traffic=models.IntegerField()



