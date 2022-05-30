from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from special.models import Masters, Persons, Specialization, Services

def special(request):
    user = request.user
    if user.is_authenticated:
        master = Masters.objects.all().first()
        try:
            master = Masters.objects.get(id=user.first_name)
        except:
            return redirect('/loginmast')
    else:
        return redirect('/register')
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            time = request.POST.get('time')
            cost = request.POST.get('cost')
            service = Services(services_name=name, cost=cost, time=time)
            service.save()
            specialization = Specialization(master = master, service=service)
            specialization.save()
            print("Done! Special")
        except Exception as e:
            print(e)
            return redirect('/special')
        return redirect('/homemaster')
    else:
        return render(request, 'special.html')
