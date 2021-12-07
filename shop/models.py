from django.db import models
from django.contrib.auth.models import User

#rom shop.views import ice_cream

#from shop.views import flavour, ice_cream, topping

class Ice_cream(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    cost = models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return self.name 

class Flavour(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    cost = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name 

class Topping(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    cost = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name 

class Milk_shake(models.Model):
    m_ice_cream = models.ForeignKey(Ice_cream,to_field='name',on_delete=None, default='none')
    m_flavour = models.ForeignKey(Flavour,to_field='name',on_delete=None, default='none')
    m_topping = models.ForeignKey(Topping,to_field='name',on_delete=None, default='none')
    m_cost = models.FloatField(null=True, blank=True, default=None) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.


