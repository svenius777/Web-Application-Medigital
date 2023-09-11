from django import forms
from django.contrib.auth.forms import UserCreationForm
from zdravstveni_sustav_app.models import Doktor

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)