from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

#edited for for registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()


    class Meta:# gives nested name space and keeps configs in one space
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']