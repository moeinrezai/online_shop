from django.shortcuts import render
from django.views.generic import TemplateView


class LogIn(TemplateView):
    template_name = 'account/contact.html'
# Create your views here.
