from django.db import models
from django.contrib.auth.models import User
from packages.models import Packages
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Clients(User):
    email = models.EmailField(_("email address"),unique=True)
    is_blocked = models.BooleanField(_("block status "),default=False)
    img = models.ImageField(_("photo"),blank=True)
    status_type=['completed','unconfirmed email']
    status=models.TextField(_("rigister status"),choices=status_type)
    def __str__(self):
        return '%s %s (%s)'%(self.first_name,self.last_name,self.username)


class Wallet(models.Model):
    id = models.AutoField(True)
    client = models.OneToOneField(
        Clients, verbose_name="wallet", on_delete=models.RESTRICT)
    balance = models.BigIntegerField(_("wallet balance"),default=0)
    createdDate = models.DateField(_("created date "),auto_now_add=True)


class incrementRequest(models.Model):
    id = models.AutoField(_("request id "),primary_key=True)
    date = models.DateField(_("request date "),auto_now_add=True)
    wallet = models.ForeignKey(
        Wallet, verbose_name='incrementRequests', on_delete=models.CASCADE)
    amount = models.BigIntegerField(_("increment mount"))
    choices = ['canceled', 'successfull', 'unsuccessfull']
    status = models.CharField(_("request status "),choices=choices)


class decrementRequest(models.Model):
    id = models.AutoField(_("request id "),primary_key=True)
    date = models.DateField(_("request date "),auto_now_add=True)
    wallet = models.ForeignKey(Wallet, verbose_name='decrementRequests', on_delete=models.CASCADE)
    amount = models.BigIntegerField(_("decrement mount"))
    choices = ['canceled', 'successfull', 'unsuccessfull']
    desc=models.TextField(_("request description"),max_length=255)
    status = models.CharField(_("request status "),choices=choices)
    package = models.OneToOneField(Packages, on_delete=models.SET_NULL)



class admins(User):
    pass