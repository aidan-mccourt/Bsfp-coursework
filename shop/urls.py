from django.urls import path
from . import views

app_name = 'shop'
#url patterns for shop pages
urlpatterns = [
    path('', views.home, name='shop-home'),
    path('ice_cream/', views.ice_cream, name='shop-ice_cream'),
    path('order_details/', views.order_details, name='shop-order_details'),
]