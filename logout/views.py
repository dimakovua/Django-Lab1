from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from django.contrib import messages

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        return redirect('register')
    else:
        return redirect('register')