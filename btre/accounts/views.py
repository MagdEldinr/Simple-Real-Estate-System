from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required   
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        #Wrong credentials
        else:
            messages.error(request, 'Please check username and password')
            return redirect('login') 
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            #Check username availability
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is not available')
                return redirect('register')
            else:
                #Check email availability
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already registered')
                    return redirect('register')
                #Data is fine
                else:
                    new_user = User.objects.create_user(first_name=first_name, last_name=last_name,
                    username=username, password=password, email=email)
                    new_user.save()
                    messages.success(request, 'Thank you')
                    return redirect('login')
        #Passwords do not match
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

