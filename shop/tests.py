from django import test
from django.contrib.auth.models import User
from django.test import TestCase


from .models import Ice_cream, Flavour, Topping, Milk_shake

class MilkShakeTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="admin")
        Ice_cream.objects.create(name="test1", cost= 1)
        Flavour.objects.create(name="test2", cost=2)
        Topping.objects.create(name="test3", cost=3)

        ice = Ice_cream.objects.get(name="test1")
        flav = Flavour.objects.get(name="test2")
        top = Topping.objects.get(name="test3")

        Milk_shake.objects.create(user=self.user1,
                            m_ice_cream= ice,
                            m_flavour = flav,
                            m_topping = top,
                            m_cost = 6)
#tests to make sure milkshakes are created properly
    def test_milk_shake_is_posted(self):
        ice = Ice_cream.objects.get(name="test1")
        """Milkshakes are created"""
        milk1 = Milk_shake.objects.get(user=self.user1)
        self.assertEqual(milk1.m_ice_cream, ice)




# Create your tests here.
