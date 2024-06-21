from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib import auth
# Create your views here.


# User Registration
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                return redirect('login_user')
            except IntegrityError:
                messages.error(request, 'Username or email already exists')
                return redirect('register_user')
        else:
            messages.info(request, 'password error')
            return redirect('register_user')
    return render(request, 'register.html')

# Login User
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, "invalid credentials")
            return redirect('login_user')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')