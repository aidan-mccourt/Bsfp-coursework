from django.shortcuts import redirect, render

from .models import Flavour, Ice_cream, Topping, Milk_shake
from django.contrib.auth.models import User


def home(request):
    
    return render(request, 'shop/home.html')
    
#views for each webpage - data from database is passed into here and then to the front end.
#logic goes here, created milkshakes are saved to data base
def ice_cream(request):




    if 'cice' and 'cflav' and 'ctop' in request.GET:
        
        cice = request.GET.getlist('cice')
        cflav = request.GET.getlist('cflav')
        ctop = request.GET.getlist('ctop')
        milk = [cice, cflav,ctop]
        request.session['x'] = milk
        return redirect('shop:shop-order_details' )

        
        
    

    context_i={
        'ice_creams' : Ice_cream.objects.all(),
        'flavours' : Flavour.objects.all(),
        'toppings' : Topping.objects.all()
        }
   
    
    return render(request, 'shop/ice_cream.html',context_i)





def order_details(request):
    milk = request.session['x']
    ice = str(milk[0])
    flav = str(milk[1])
    top = str(milk[2])
    ice2 = ice[2:len(ice)-2]
    flav2 = flav[2:len(flav)-2]
    top2 =top[2:len(top)-2]

    ice_v = Ice_cream.objects.get(name=ice2)
    ice_cost = ice_v.cost
    flav_v = Flavour.objects.get(name=flav2)
    flav_cost = flav_v.cost
    top_v = Topping.objects.get(name=top2)
    top_cost = top_v.cost

    total_cost = ice_cost + flav_cost + top_cost
    currentu = request.user

    m = Milk_shake(m_ice_cream = ice_v, m_flavour = flav_v, m_topping = top_v, m_cost = total_cost, user = currentu)
   

    context_m={
        'milk_shakes' : Milk_shake.objects.all(),
        'cice' : ice2,
        'cflav' :flav2,
        'ctop' : top2,
        'tot' : total_cost
    }

    if request.method == 'POST':
        m.save()
        return redirect('shop:shop-home') 

    return render(request, 'shop/order_details.html', context_m)
# Create your views here.
