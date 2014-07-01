from django import forms
from django.forms import ModelForm
from products.models import Product


class ProductAddForm(ModelForm):
    name = forms.CharField(label=(u'Name'))
    price = forms.FloatField(label=(u'Price'))
    stock = forms.IntegerField(label=(u'Stock'))
    limit = forms.IntegerField(label=(u'Limit'))

    class Meta:
        model = Product