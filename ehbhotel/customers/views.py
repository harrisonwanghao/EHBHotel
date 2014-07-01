# coding: utf-8

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from reportlab.pdfgen import canvas
from io import BytesIO
from django.core.mail import EmailMessage
from customers.forms import RegistrationForm
from customers.forms import LoginForm
from customers.models import Customer
from transactions.models import Transaction

# Create your views here.

def CustomerRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/customer/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            birth = form.cleaned_data['birth']
            address = form.cleaned_data['address']
            special = form.cleaned_data['special_request']
            user = Customer.objects.create_user(email=email, password=password, first=first, last=last, birth=birth, address=address, special=special, used=None)
            return HttpResponseRedirect('/customer/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))


def CustomerLogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/customer/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            customer = authenticate(email=email, password=password)
            if customer is not None:
                login(request, customer)
                return HttpResponseRedirect('/customer/')
            else:
                return HttpResponseRedirect('/customer/login/')
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))


def CustomerProfile(request):
    if request.user.is_authenticated():
        return render_to_response('profile.html', None, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/customer/login/')


def CustomerLogout(request):
    logout(request)
    return HttpResponseRedirect('/customer/login/')

def CustomerInvoice(request):
    if request.method == 'POST':
        transactions = Transaction.objects.filter(customer=request.user)
        total = 0
        products = []
        for transaction in transactions:
            products += transaction.products.all()
        for product in products:
            total += product.price
        lastname = "Naam: {}".format(request.user.last_name)
        firstname = "Voornaam: {}".format(request.user.first_name)
        address = "Adres: {}".format(request.user.address)
        cost = "Te betalen: €{}".format(total)
        url = './static/customers/logo.jpg'

        if 'email' in request.POST:
            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            p.drawString(10, 830, lastname)
            p.drawString(10, 820, firstname)
            p.drawString(10, 810, address)
            p.drawString(10, 800, cost)
            p.drawImage(url, 450, 740, 100, 100)
            p.showPage()
            p.save()
            pdf = buffer.getvalue()
            buffer.close()
            body = "Beste {},\nIn de bijlage vindt u uw factuur van het EHBHotel. Wij hopen u snel weer te zien.\nMet vriendelijke groeten,\nEHBHotel".format(request.user.first_name + " " + request.user.last_name)
            message = EmailMessage("EHBHotel Factuur", body,  "factuur@ehbhotel.com", [request.user.email,])
            message.attach('invoice.pdf', pdf, 'application/pdf')
            message.send()
            return HttpResponseRedirect('/customer/')

        if 'download' in request.POST:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
            p = canvas.Canvas(response)
            p.drawString(10, 830, lastname)
            p.drawString(10, 820, firstname)
            p.drawString(10, 810, address)
            p.drawString(10, 800, cost)
            p.drawImage(url, 450, 740, 100, 100)
            p.showPage()
            p.save()
            return response
    else:
        return HttpResponseRedirect('/customer/')