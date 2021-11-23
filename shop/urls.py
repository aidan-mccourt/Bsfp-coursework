from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('ice_cream/', views.ice_cream, name='shop-ice_cream'),
    path('user_details/', views.user_details, name='shop-user_details'),
    path('flavour/', views.flavour, name='shop-flavour'),
    path('topping/', views.topping, name='shop-topping'),
    path('order_details/', views.order_details, name='shop-order_details'),
]