from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .forms import LoginForm
from django.contrib.auth import authenticate, login
# class LogIn(TemplateView):
    # template_name = 'account/login.html'
# Create your views here.
class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})\


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