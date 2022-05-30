from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Clients.models import Clients, Persons, Specialization, Services, Devices, OwnershipDocument, Masters, Contract, ContractNew1
from datetime import date

class DeviceAndServices:
    def __init__(self, device, services):
        self.device = device
        self.services = services
def CheckDevice(client, device):
    device_id = device.id
    list_devices = []
    try:
        list_devices = ContractNew1.objects.all().filter(device=device_id, client=client.id)
    except:
        list_devices = []
    if len(list_devices) == 0:
        return True
    else:
        return False
def choose(request):
    if request.user.is_authenticated:
        client = Clients.objects.all().first()
        try:
            client = Clients.objects.get(email=request.user.email)
        except Exception as e:
            print(e)
            return redirect('logincl')
        list_of_problems = []
        list_of_ownerships = OwnershipDocument.objects.all().filter(owner=client)
        if len(list_of_ownerships) == 0:
        #     for i in list_of_ownerships:
        #         list_of_problems.append(i.device.breakage)
        # else:
            return redirect('adddevices')
        # list_of_services = []
        # for i in list_of_problems:
        #     listt = Services.objects.all().filter(serices_name=i.name)
        #     list_of_services.append(listt)
        result = []
        for i in list_of_ownerships:
            listt = Services.objects.all().filter(services_name=i.device.breakage)
            if CheckDevice(client, i.device):
                result.append(DeviceAndServices(device=i.device, services=listt))
        return render(request, 'choose.html', {'class' : result})
    else:
        return redirect('logincl')

def offer(request, dev_id, serv_id):
    print("Offering")
    if request.user.is_authenticated:
        client = Clients.objects.all().first()
        try:
            client = Clients.objects.get(email=request.user.email)
        except Exception as e:
            print(e)
            return redirect('logincl')
        try:
            service = Services.objects.get(id=serv_id)
            device = Devices.objects.get(id=dev_id)
            status = 1
            datee = date.today()
            spec = Specialization.objects.get(service=service)
            master = spec.master
            contractnew = ContractNew1(service=service.id, master=master.id, client=client.id, status=status, date=datee, device=device.id)
            contract = Contract(service=service, status=status, date=datee, master=master, client=client)
            contract.save()
            contractnew.save()
        except Exception as e:
            print(e)
        return redirect('homeclient')
    else:
        return redirect('logincl')