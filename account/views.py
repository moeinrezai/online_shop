from random import randint
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
import requests

import ghasedakpack
sms = ghasedakpack.Ghasedak(apikey='495df957a36aaa2f58a051a28dbcc17b96f1b9a6b85ca9f075a7470edd8b29c1seobCY2G5nh6AvzP')
# class LogIn(TemplateView):
    # template_name = 'account/login.html'
# Create your views here.
class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                form.add_error("phone", "invalid user data")

        else:
            form.add_error("phone", "invalid data")

        return render(request, "account/login.html", {'form': form})




class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            randcode = randint(1000,9999)
            cd = form.cleaned_data

            sms.verification({'receptor': cd["phone"], 'type': '1', 'template': 'Ghasedak', 'parm1': randcode})



        else:
            form.add_error("phone", "invalid data")

        return render(request, "account/login.html", {'form': form})