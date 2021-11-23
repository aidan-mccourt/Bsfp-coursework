from django.contrib import admin
from .models import Flavour,Ice_cream,Topping, Milk_shake

admin.site.register(Flavour)
admin.site.register(Ice_cream)
admin.site.register(Topping)
admin.site.register(Milk_shake)

# Register your models here.
#adds them to admin page