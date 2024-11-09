from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password']
