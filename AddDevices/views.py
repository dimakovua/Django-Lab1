from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from homeClients.models import Clients, Persons, Devices, OwnershipDocument
# Create your views here.

def adddevices(request):
    if request.user.is_authenticated:
        user = request.user
        client = Clients.objects.get(email=user.email)
        if request.method == 'POST':
            name = request.POST.get('name')
            model = request.POST.get('model')
            breakage = request.POST.get('breakage')
            device = Devices(name=name, model=model, breakage=breakage)
            device.save()
            ownership = OwnershipDocument(device=device, owner=client)
            ownership.save()
            print("OK")
            return redirect('/homeclient')
        else:
            return render(request, 'adddevices.html')
    else:
        return redirect('/clientreg')