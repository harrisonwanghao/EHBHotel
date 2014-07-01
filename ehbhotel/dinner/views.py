from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customer
import goslate


def Translate(request):
    gs = goslate.Goslate()
    return HttpResponse("Origineel: Hallo liefste wereld. Vertaald:" + gs.translate('hallo liefste wereld', 'en', 'nl'))

def Index(request):
    return render(request, 'welcome.html')

def Resto(request):
    return render(request, 'resto.html')

def Menu(request):
    return render(request, 'menu.html')

def Gallery(request):
    return render(request, 'gallery.html')

def Info(request):
    return render(request, 'info.html')

def Contact(request):
    return render(request, 'contact.html')