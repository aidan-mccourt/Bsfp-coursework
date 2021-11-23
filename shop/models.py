from django.db import models
from django.contrib.auth.models import User

from shop.views import ice_cream

#from shop.views import flavour, ice_cream, topping

class Ice_cream(models.Model):
    name = models.CharField(max_length = 100)
    cost = models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return self.name 

class Flavour(models.Model):
    name = models.CharField(max_length = 100)
    cost = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name 

class Topping(models.Model):
    name = models.CharField(max_length = 100)
    cost = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name 

class Milk_shake(models.Model):
    m_ice_cream = models.ForeignKey(Ice_cream,on_delete=None)
    m_flavour = models.ForeignKey(Flavour,on_delete=None)
    m_topping = models.ForeignKey(Topping,on_delete=None)
    m_cost = models.FloatField(null=True, blank=True, default=None) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.


