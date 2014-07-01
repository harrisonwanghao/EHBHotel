from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from reservations.forms import ReservationAddForm
from reservations.models import Reservation


def ReservationAdd(request):
    if request.user.is_authenticated and request.user.ad:
        if request.method == 'POST':
            form = ReservationAddForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/reservations/')
            else:
                return render_to_response('addreservation.html', {'form': form, 'errors': form.errors}, context_instance=RequestContext(request))

        else:
            form = ReservationAddForm()
            context = {'form': form}
            return render_to_response('addreservation.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


def ReservationList(request):
    if request.user.is_authenticated and request.user.ad:
        return render_to_response('reservations.html', {'reservations': Reservation.objects.all()}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')