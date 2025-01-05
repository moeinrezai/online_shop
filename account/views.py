from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import LoginForm

# class LogIn(TemplateView):
    # template_name = 'account/login.html'
# Create your views here.

class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


