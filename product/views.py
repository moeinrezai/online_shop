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

    def get_context_data(self, **kwargs):
        request = self.request
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        contex = super(ProductsListView, self).get_context_data()
        contex['object_list'] = Product.objects.all()
        return contex