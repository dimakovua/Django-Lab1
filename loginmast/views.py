from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from masterreg.models import Masters, Persons
def loginmast(request):
    if request.method == 'POST':
        print("ABOBA")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            try:
                mast = Masters.objects.get(id = user.first_name)
            except:
                messages.info(request, "Couldn\'t login")
                return redirect('/loginmast')
            auth.login(request, user)
            return redirect('/homemaster')
        else:
            messages.info(request, "Couldn\'t login")
            return redirect('/loginmast')
    else:
        return render(request, 'login_client.html')
# Create your views here.
