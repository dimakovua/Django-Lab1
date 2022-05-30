import re
from django.shortcuts import render, HttpResponse

def homemaster(request):
    return render(request, 'homemasters.html')
