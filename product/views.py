from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from .models import Product, Category


class ProductView(DetailView):
    template_name = "product/detail.html"
    model = Product


class NavbarPartialView(TemplateView):
    template_name = 'includes/navbar.html'

    def get_context_data(self, **kwargs):
        contex = super(NavbarPartialView, self).get_context_data()
        contex['categories'] = Category.objects.all()
        return contex

class ProductsListView(ListView):
    template_name = 'product/product_list.html'
    queryset = Product.objects.all()
