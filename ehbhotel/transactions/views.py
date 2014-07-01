from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from transactions.forms import TransactionAddForm
from transactions.models import Transaction


def TransactionAdd(request):
    if request.user.is_authenticated and request.user.ad:
        if request.method == 'POST':
            form = TransactionAddForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/transactions/')
            else:
                return render_to_response('addtransaction.html', {'form': form}, context_instance=RequestContext(request))

        else:
            form = TransactionAddForm()
            context = {'form': form}
            return render_to_response('addtransaction.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


def TransactionList(request):
    if request.user.is_authenticated and request.user.ad:
        return render_to_response('transactions.html', {'transactions': Transaction.objects.all()}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')