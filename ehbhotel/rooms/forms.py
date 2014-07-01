from django import forms
from django.forms import ModelForm
from rooms.models import Room



class RoomAddForm(ModelForm):
    number = forms.IntegerField(label=(u'Room number'))
    capacity = forms.IntegerField(label=(u'Capacity'))
    floor = forms.IntegerField(label=(u'Floor number'))

    class Meta:
        model = Room