import re
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from homeMasters.models import Masters, Persons, Services, Specialization, Contract, ContractNew1

def done(request, contr_id):
    contr = Contract.objects.get(id=contr_id)
    contrnew = ContractNew1.objects.get(id=int(contr.id-2))
    contr.status = 3
    contrnew.status = 3
    contr.save()
    contrnew.save()
    return redirect('/homemaster')
def delete_item(request, id):
    service = Services.objects.get(id=id)
    special = Specialization.objects.get(service=service)
    special.delete()
    service.delete()
    print("Done!")
    return redirect('/homemaster')

def homemaster(request):
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
        list_services = []
        if len(list_specializations) != 0:
            for i in list_specializations:
                list_services.append(i.service)
                print(i.service.services_name)
        contracts = Contract.objects.all().filter(master=master, status=2)

        return render(request, 'homemasters.html', {'service' : list_services, 'name' : master.person.first_name, 'contracts' : contracts})
    else:
        return redirect('register')