from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
print(settings.TEMPLATES[0]['DIRS'])

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')
