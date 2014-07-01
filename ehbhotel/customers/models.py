from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from products.models import Product


class CustomerManager(BaseUserManager):
    def create_user(self, email,
                    password=None, first=None, last=None, birth=None, address=None, special=None, used=None, ad=False):
        user = self.model(email=email)
        user.set_password(password)
        user.first_name = first
        user.last_name = last
        user.date_of_birth = birth
        user.address = address
        user.special_request = special
        user.used_products = used
        user.ad = ad
        user.save()
        return user

    def create_superuser(self, email,
                    password=None):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

class Customer(AbstractBaseUser):
    def __str__(self):
        return str(self.email)

    email = models.CharField(max_length=100, primary_key=True)
    USERNAME_FIELD = 'email'
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200)
    special_request = models.CharField(max_length=200, null=True, blank=True)
    used_products = models.ForeignKey(Product, null=True, blank=True)
    ad = models.BooleanField(default=False)
    objects = CustomerManager()