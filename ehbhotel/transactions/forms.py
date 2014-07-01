from django import forms
from django.forms import ModelForm
from transactions.models import Transaction
from products.models import Product
from customers.models import Customer


class TransactionAddForm(ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.widgets.CheckboxSelectMultiple)

    class Meta:
        model = Transaction