#import email
#from typing_extensions import Self
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

#def email_check(user):
#   return user.email.endswith('@admin2.com')
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        #print(request.POST.get('email'))
        #print(request.POST.get('password'))
        #print(request.POST.get('signin'))
        #print(request.POST)
        #print('obteniendo datos')
        #user = User.get_username(email=request.POST.get('email'))
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('crear_torneo')
        else:
            return render(request, 'login.html')


    
#@login_required(redirect_field_name='home')

def crear_torneo(request):
    #print(request.user.is_authenticated)
    #print(request.user.is_anonymous)
    if not request.user.is_anonymous:
        if not request.user.email.endswith('@admin.com'):
            return redirect('login')
        else:
            return render(request, 'crearTorneo.html')
    else:
        return redirect('login')