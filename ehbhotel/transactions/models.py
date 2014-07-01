from django.db import models
from products.models import Product
from customers.models import Customer

class Transaction(models.Model):
    customer = models.ForeignKey(Customer)
    products = models.ManyToManyField(Product)
