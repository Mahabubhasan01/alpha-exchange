from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from api.models import Order


class Register_User(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'type strong password'}))
    password2 = forms.CharField(
        label='Password(again)', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ['username',  'email']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name', 'email': 'Email', }
        widgets = {'username': forms.TextInput(attrs={'class': 'input-field  ', 'placeholder': 'username'}),
                   'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'type valid email'}), }


class Order_Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class Login_Form(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'w-full text-base px-4 py-2 bg-gray-900 border border-gray-700 rounded-lg focus:outline-none focus:border-purple-400', 'placeholder': 'username'}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(
        attrs={'class': 'w-full content-center text-base px-4 py-2 bg-gray-900 border border-gray-700 rounded-lg focus:outline-none focus:border-purple-400', 'autocomplete': 'off'}))
