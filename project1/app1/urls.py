from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.signup,name='signup'),
    path('login',views.loginPage,name='login')
]