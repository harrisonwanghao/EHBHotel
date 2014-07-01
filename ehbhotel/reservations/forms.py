from django import forms
from django.forms import ModelForm
from reservations.models import Reservation
from rooms.models import Room
from customers.models import Customer
from ehbhotel import settings


class ReservationAddForm(ModelForm):
    startDate = forms.DateField(label=(u'Start date:'), input_formats=settings.DATE_INPUT_FORMATS)
    endDate = forms.DateField(label=(u'End date:'), input_formats=settings.DATE_INPUT_FORMATS)
    room = forms.ModelChoiceField(queryset=Room.objects.all())
    guests = forms.ModelMultipleChoiceField(queryset=Customer.objects.all(), widget=forms.widgets.CheckboxSelectMultiple)

    class Meta:
        model = Reservation