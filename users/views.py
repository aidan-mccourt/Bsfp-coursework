from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
#user views for registration form
def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()# auto matically hashes passwords for the account
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created, please log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required #decorator adds functionality to profile view, users has to be logged in
def user_details(request):
    return render(request, 'users/user_details.html')

# Create your views here.
