from django.contrib.auth.views import LoginView
from django.shortcuts import render

from .forms import LoginUserForm


# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'