from django.db import models
from django.contrib.auth.models import User
from packages.models import Packages

# Create your models here.


class Clients(User):
    is_blocked = models.BooleanField(default=False)
    img = models.ImageField(blank=True)


class Wallet(models.Model):
    id = models.AutoField(True)
    client = models.OneToOneField(
        Clients, verbose_name="wallet", on_delete=models.RESTRICT)
    balance = models.BigIntegerField(default=0)
    createdDate = models.DateField(auto_now_add=True)


class incrementRequest(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    wallet = models.ForeignKey(
        Wallet, verbose_name='incrementRequests', on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    choices = ['canceled', 'successfull', 'unsuccessfull']
    status = models.CharField(choices=choices)


class decrementRequest(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    wallet = models.ForeignKey(Wallet, verbose_name='decrementRequests', on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    choices = ['canceled', 'successfull', 'unsuccessfull']
    desc=models.TextField(max_length=255)
    status = models.CharField(choices=choices)
    package = models.OneToOneField(Packages, on_delete=models.SET_NULL)



class admins(User):
    pass