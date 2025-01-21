from random import randint
from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import LoginForm, OtpLoginForm, CheckOtpForm, AddressCreationForm
from django.contrib.auth import authenticate, login, logout
from uuid import uuid4
from .models import Otp, User
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
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('/')

            else:
                form.add_error("phone", "invalid user data")

        else:
            form.add_error("phone", "invalid data")

        return render(request, "account/login.html", {'form': form})




class Otp_LoginView(View):
    def get(self, request):
        form = OtpLoginForm()
        return render(request, 'account/otp_login.html', {'form': form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000,9999)
            sms.verification({'receptor': cd["phone"], 'type': '1', 'template': 'Ghasedak', 'param1': randcode})
            print(randcode)
            token = str(uuid4())
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)

            return redirect(reverse('account:check_otp') + f'?token={token}')


        else:
            form.add_error("phone", "invalid data")

        return render(request, "account/otp_login.html", {'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/check_otp.html', {'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_create = User.objects.get_or_create(phone=otp.phone)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect('/')
        else:
            form.add_error("phone", "invalid data")

        return render(request, "account/check_otp.html", {'form': form})

class AddAddressView(View):
    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)

        return render(request, 'account/add_address.html', {'form': form})

    def get(self, request):
        form = AddressCreationForm
        return render(request, 'account/add_address.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')