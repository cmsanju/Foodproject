from django.shortcuts import render,redirect
from django.views import View
from Admin.models import Admin

from django.contrib import messages
# Create your views here.
def admin_login(request):
    return render(request,'Admin_login.html')

def admin_home(request):
    return render(request,'Admin_home.html')

def all_users(request):
    return render(request,'All_users.html')

def admin_login_verification(request):
    if request.method=="POST":
        try:
            email=request.POST['email']
            password=request.POST['password']
            storage=messages.get_messages(request)
            storage.used=True
            if Admin.objects.filter(email=email,password=password):
                request.session['email']=email
                return redirect('admin_home')
            else:
                messages.info(request,"Username or password does not match")
                return redirect('admin_login')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')