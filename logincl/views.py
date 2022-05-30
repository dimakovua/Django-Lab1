from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from clientreg.models import Clients, Persons
def logincl(request):
    if request.method == 'POST':
        print("ABOBA")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            try:
                client = Clients.objects.get(email=user.email)
            except:
                messages.info(request, "Couldn\'t login")
                return redirect('/logincl')
            auth.login(request, user)
            return redirect('/homeclient')
        else:
            messages.info(request, "Couldn\'t login")
            return redirect('/logincl')
    else:
        return render(request, 'login_client.html')
# Create your views here.
