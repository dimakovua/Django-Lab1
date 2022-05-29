from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
def logincl(request):
    if request.method == 'POST':
        print("ABOBA")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/homeclient')
        else:
            messages.info(request, "Couldn\'t login")
            return redirect('/logincl')
    else:
        return render(request, 'login_client.html')
# Create your views here.
