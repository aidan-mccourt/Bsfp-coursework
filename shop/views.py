from django.shortcuts import render
from django.http import HttpResponse
#from .models import Flavour#, Ice_cream, Topping, Milk_shake
#import models

def home(request):
    return render(request, 'shop/home.html')

def ice_cream(request):
    context_i={
        'ice_creams' : Ice_cream.objects.all()
    }
    return render(request, 'shop/ice_cream.html',context_i)

def user_details(request):
    return render(request, 'shop/user_details.html')

def flavour(request):
    context ={
        'flavours' : Flavour.objects.all()
    }#need to look at how to do code stuff regarding flavours in html page.
    return render(request, 'shop/flavour.html', context)

def topping(request):
    context_t={
        'toppings' : Topping.objects.all()
    }
    return render(request, 'shop/topping.html',context_t)

def order_details(request):
    context_m={
        'milk_shakes' : Milk_shake.objects.all()
    }
    return render(request, 'shop/order_details.html', context_m)
# Create your views here.
