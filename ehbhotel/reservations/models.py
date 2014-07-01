from django.db import models
from rooms.models import Room
from customers.models import Customer
from django.contrib.auth.models import User


class Reservation(models.Model):
    def __str__(self):
        return str(self.startDate)

    startDate = models.DateField()
    endDate = models.DateField()
    room = models.ForeignKey(Room)
    guests = models.ManyToManyField(Customer)