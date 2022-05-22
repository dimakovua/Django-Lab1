from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
def clientreg(request):
    print("ABOBA")
    if request.method == 'POST':
        print("ABOBA")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        if password1 == password2:
            print(password1, password2)
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
                return redirect('/clientreg')
            elif User.objects.filter(email=email).exists(): 
                messages.info(request, 'Email is taken')
                return redirect('/clientreg')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print ('User created')
                return redirect('/home')  
        else:
            print('im here')
            messages.info(request, 'Password does not match')    
            return redirect('/clientreg')
    else:
        return render(request, 'clientreg.html')
