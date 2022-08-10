from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms


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
