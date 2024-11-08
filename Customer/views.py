from django.shortcuts import render,redirect
from django.views import View
from Customer.models import Customer
from Restaurant.models import Restaurant

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'Home.html')

def error(request):
    return render(request,'Error.html')

def something_went_wrong(request):
    return render(request,'Something_went_wrong.html')

def register(request):
    return render(request,'Register.html')

def user_registration(request):
    return render(request,'Customer_registration.html')

def user_login(request):
    return render(request,'User_login.html')

def my_profile(request):
    email=request.session.get('email')
    if request.session and Customer.objects.filter(email=email).exists():
        customer=Customer.objects.get(email=email)
        data={'cus_name':customer.name,'cus_profile_picture':customer.profile_picture,'cus_email':customer.email,'cus_address':customer.address,'cus_mobilenumber':customer.mobile_number}
        return render(request,'My_profile.html',data)
    else:
        return redirect('error')

def cus_home(request):
    email=request.session.get('email')
    if request.session and Customer.objects.filter(email=email).exists():
        customer=Customer.objects.get(email=email)
        data={'cus_name':customer.name}
        return render(request,'Customer_home.html',data)
    else:
        return redirect('error')
    
def view_orders_cus(request):
    return render(request,'View_orders_cus.html')

def feedback_cus(request):
    return render(request,'Feedback_cus.html')

def logout(req):
    try:
        del req.session['email']
    except KeyError:
        pass
    return redirect('/')


# REST APIs
def create_customer(request):
    if request.method=="POST":
        try:    
            name=request.POST['name']
            profile_picture=request.FILES['profile_picture']
            email=request.POST['email']
            password=request.POST['password']
            mobilenumber=request.POST['mobilenumber']
            address=request.POST['address']
            Customer.objects.create(name=name,profile_picture=profile_picture,email=email,password=password,mobile_number=mobilenumber,address=address)
            return redirect('user_login')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')
    
def login_verification(request):
    if request.method=="POST":
        try:
            role=request.POST['role']
            email=request.POST['email']
            password=request.POST['password']
            storage=messages.get_messages(request)
            storage.used=True
            if role=='customer':
                if(Customer.objects.filter(email=email,password=password)):
                    request.session['email']=email
                    return redirect('cus_home')
                else:
                    messages.info(request,"Username or password does not match")
                    return redirect('user_login')
            elif role=='restaurant':
                if(Restaurant.objects.filter(email=email,password=password)):
                    request.session['email']=email
                    return redirect('res_home')
                else:
                    messages.info(request,"Username or password does not match")
                    return redirect('user_login')
            elif role=='delivery':
                return redirect('/')
            else:
                return redirect('/')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')

