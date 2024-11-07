from django.shortcuts import render
from django.views import View

# Create your views here.
def admin_login(request):
    return render(request,'Admin_login.html')