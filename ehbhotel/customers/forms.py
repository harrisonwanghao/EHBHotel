from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from customers.models import Customer


class RegistrationForm(ModelForm):
    email = forms.EmailField(label=(u'Email'))
    first_name = forms.CharField(label=(u'First name'))
    last_name = forms.CharField(label=(u'Last name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    address = forms.CharField(label=(u'Address'))
    birth = forms.DateField(label=(u'Date of birth'), widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y',))

    class Meta:
        model = Customer
        exclude = ('used_products', 'last_login')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, please select another.")


class LoginForm(forms.Form):
    email = forms.CharField(label=(u'Email'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))