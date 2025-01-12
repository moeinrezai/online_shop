from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.UserLogin.as_view(), name='login'),
    path('otplogin', views.Otp_LoginView.as_view(), name='user_otp_login'),
    path('checkotp', views.CheckOtpView.as_view(), name='check_otp'),
    path('logout', views.user_logout, name='logout'),
]