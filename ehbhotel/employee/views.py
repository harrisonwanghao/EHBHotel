from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from ldap3 import LDAPException
from employee.forms import LoginForm
# Create your views here.

def EmployeeProfile(request):
    if request.user.is_authenticated():
        if request.user.ad:
            return render_to_response('profileemp.html', None, context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/employee/login/')


def EmployeeLogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/employee/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            employee = authenticate(username = username, password = password)
            if employee is not None:
                login(request, employee)
                return HttpResponseRedirect('/employee/')
            else:
                return HttpResponseRedirect('/employee/login/')
        else:
            return render_to_response('loginemp.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response('loginemp.html', context, context_instance=RequestContext(request))

def EmployeeLogout(request):
    logout(request)
    return HttpResponseRedirect('/employee/login/')

def Preparation(request):
    if request.user.is_authenticated and request.user.ad:
        return render(request, 'bereiding.html')
    else:
        return HttpResponseRedirect('/')

def Dessert(request):
    if request.user.is_authenticated and request.user.ad:
        return render(request, 'dessert.html')
    else:
        return HttpResponseRedirect('/')

def Main(request):
    if request.user.is_authenticated and request.user.ad:
        return render(request, 'hoofdgerecht.html')
    else:
        return HttpResponseRedirect('/')

def Menu(request):
    if request.user.is_authenticated and request.user.ad:
        return render(request, 'menuemp.html')
    else:
        return HttpResponseRedirect('/')

def Starter(request):
    if request.user.is_authenticated and request.user.ad:
        return render(request, 'voorgerecht.html')
    else:
        return HttpResponseRedirect('/')

