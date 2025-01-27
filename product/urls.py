from django.urls import path
from . import views
from .views import NavbarPartialView

app_name = 'product'
urlpatterns = [
    path('all', views.ProductListView.as_view(), name="product_list"),
    path('<int:pk>', views.ProductView.as_view(), name="product_detail"),
    path('navbar', NavbarPartialView.as_view(), name="navbar"),
]