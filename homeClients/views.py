from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from homeClients.models import Clients, Persons, Devices, OwnershipDocument, Contract, Masters, Services, Specialization, OwnershipDocument, ContractNew1
# Create your views here.

def delete_item(request, id):
    device = Devices.objects.get(id=id)
    owndoc = OwnershipDocument.objects.get(device=device)
    contrnew = ContractNew1.objects.get(device=device.id)
    contr = Contract.objects.get(id=int(contrnew.id+2))
    contrnew.delete()
    contr.delete()
    owndoc.delete()
    device.delete()
    print("deleted")
    return redirect('/homeclient')


def homeclient(request):
    if request.user.is_authenticated:
        client = Clients.objects.all().first()
        email = request.user.email
        try:
            client = Clients.objects.get(email=email)
            print(client.person.first_name)
        except:
            return redirect('/homemaster')
        client_id = client.id
        list_ownerships = []
        try:
            list_ownerships = OwnershipDocument.objects.filter(owner=client)
        except:
            print("Exception")
            list_ownerships = []
        print(list_ownerships)
        list_devices = []
        if len(list_ownerships) != 0 : ##NOT A LIST!!!!!!!!!!!!!!!!!!!
            list_devices = []
            for i in list_ownerships :
                list_devices.append(i.device)
                print(i.device.name)
        contracts = Contract.objects.all().filter(client=client, status=1)
        contracts_progress = Contract.objects.all().filter(client=client, status=2)
        contracts_done = Contract.objects.all().filter(client=client, status=3)
        return render(request, 'homeclients.html', {'name': client.person.first_name, 'devices' : list_devices, 'contracts': contracts, 'contracts_progress': contracts_progress, 'contracts_done' : contracts_done})
    else:
        return redirect('/clientreg')
