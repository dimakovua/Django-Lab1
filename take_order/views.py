import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Clients.models import Clients, Persons, Specialization, Services, Devices, OwnershipDocument, Masters, Contract, ContractNew1
from datetime import date

def take(request, contr_id):
    contr = Contract.objects.get(id=contr_id)
    contrnew = ContractNew1.objects.get(id=int(contr.id-2))
    contr.status = 2
    contrnew.status = 2
    contr.save()
    contrnew.save()
    return redirect('take-order')

def refuse(request, contr_id):
    contr = Contract.objects.get(id=contr_id)
    contrnew = ContractNew1.objects.get(id=int(contr.id-2))
    contr.delete()
    contrnew.delete()
    return redirect('take-order')

def take_order(request):
    if request.user.is_authenticated:
        master = Masters.objects.all().first()
        user = request.user
        try:
            master = Masters.objects.get(id=user.first_name)
        except:
            return redirect('loginmast')
        
        list_specializations = []
        try:
            list_specializations = Specialization.objects.all().filter(master=master)
        except:
            list_specializations = []
        list_of_services = []
        list_of_services_name = []
        for i in list_specializations:
            list_of_services.append(i.service)
            list_of_services_name.append(i.service.services_name)
        list_of_contracts = []
        try:
            list_of_contracts = Contract.objects.all().filter(status=1, master=master)
        except:
            list_of_contracts = []
        res = []
        for i in list_of_contracts:
            if i.service.services_name in list_of_services_name:
                res.append(i)
        
        return render(request, 'take_order.html', {'contracts': res})

    else:
        return redirect('loginmast')
