from django.db import models

class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=9999)
    price = models.FloatField()
    stock = models.IntegerField()
    limit = models.IntegerField()

