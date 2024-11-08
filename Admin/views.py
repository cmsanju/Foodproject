from django.shortcuts import render
from django.views import View

# Create your views here.
def admin_login(request):
    return render(request,'Admin_login.html')

def admin_home(request):
    return render(request,'Admin_home.html')

def all_users(request):
    return render(request,'All_users.html')