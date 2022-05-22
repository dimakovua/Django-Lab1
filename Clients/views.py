from django.shortcuts import render
from .models import Clients, Persons

def display_client(request):
    per = Persons.objects.all()
    cl = Clients.objects.all()
    return render(request, 'table_client.html', {'cl': cl, 'per': per})
# Create your views here.
