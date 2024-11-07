from django.shortcuts import render
from django.views import View

# Create your views here.
def home(request):
    return render(request,'Home.html')

def register(request):
    return render(request,'Register.html')

def user_registration(request):
    return render(request,'Customer_registration.html')

def user_login(request):
    return render(request,'User_login.html')

