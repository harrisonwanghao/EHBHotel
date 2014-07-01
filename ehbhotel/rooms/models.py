from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    def __str__(self):
        return str(self.number)

    number = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    floor = models.IntegerField()

