from django.shortcuts import render,redirect
from django.views import View

from Restaurant.models import Restaurant

# Create your views here.
def res_registration(request):
    return render(request,'Restaurant_register.html')

def res_home(request):
    email=request.session.get('email')
    if request.session and Restaurant.objects.filter(email=email).exists():
        restaurant=Restaurant.objects.get(email=email)
        data={'res_name':restaurant}
        return render(request,'Restaurant_home.html',data)
    else:
        return redirect('error')   

def add_food(request):
    return render(request,'Add_food.html')

def view_orders(request):
    return render(request,'View_orders.html')

def add_delivery_partner(request):
    return render(request,'Add_delivery_partner.html')

def check_feedback(request):
    return render(request,'Check_feedback.html')

# REST APTs
def create_restaurant(request):
    if request.method=="POST":
        try:    
            name=request.POST['name']
            restaurant_picture=request.FILES['restaurant_picture']
            address=request.POST['address']
            mobilenumber=request.POST['mobilenumber']
            email=request.POST['email']
            password=request.POST['password']
            Restaurant.objects.create(res_name=name,restaurant_picture=restaurant_picture,email=email,password=password,mobile_number=mobilenumber,address=address)
            return redirect('user_login')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')