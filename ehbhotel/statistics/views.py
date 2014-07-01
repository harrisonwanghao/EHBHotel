from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from reservations.models import Reservation
from customers.models import Customer

def Overview(request):
    if request.user.is_authenticated and request.user.ad:
        class CustomerReservationData(object):
            def __init__(self, **kwargs):
                self.__dict__.update(kwargs)
        dataList = []
        usedCustomers = []
        customerReservationData = CustomerReservationData(customer = Customer(),
                                                      amountReservations = 0)
        reservations = Reservation.objects.all()
        reservationAmount = Reservation.objects.all().count()
        reservationAmount2 = reservationAmount / 2
        for reservation in reservations:
            for customer in reservation.guests.all():
                if customer not in usedCustomers:
                    customerReservationData.customer = customer
                    customerReservationData.amountReservations = Reservation.objects.filter(guests=customer).count() / Reservation.objects.all().count() * 100
                    dataList.append(customerReservationData)
                    usedCustomers.append(customer)
        return render_to_response('overview.html', {'data': dataList, 'reservations': reservationAmount, 'reservations2': reservationAmount2}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')
