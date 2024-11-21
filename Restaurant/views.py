from django.shortcuts import render,redirect
from django.views import View

from Restaurant.models import Restaurant,Food
from Delivery.models import Delivery_Person
from django.contrib import messages
from django.db.models import Q
from Customer.models import Feedback

# Create your views here.
def res_registration(request):
    return render(request,'Restaurant_register.html')

def res_home(request):
    email=request.session.get('email')
    if request.session and Restaurant.objects.filter(email=email).exists():
        restaurant=Restaurant.objects.get(email=email)
        foods=Food.objects.filter(food_by=restaurant.res_name)
        data={'res_name':restaurant,'foods':foods}
        return render(request,'Restaurant_home.html',data)
    else:
        return redirect('error')   

def add_food(request):
    email=request.session.get('email')
    if request.session and Restaurant.objects.filter(email=email).exists():
        obj=Restaurant.objects.get(email=email)
        data={'name':obj.res_name}
        return render(request,'Add_food.html',data)
    else:
        return redirect('error')

def view_orders(request):
    return render(request,'View_orders.html')

def add_delivery_partner(request):
    email=request.session.get('email')
    if request.session and Restaurant.objects.filter(email=email).exists():
        working=Restaurant.objects.get(email=email)
        return render(request,'Add_delivery_partner.html',{'working':working})
    else:
        return redirect('error')

def check_feedback(request):
    email=request.session.get('email')
    if request.session and Restaurant.objects.filter(email=email).exists():
        res_name=Restaurant.objects.get(email=email)
        feedback=Feedback.objects.exclude(Q(admin_feedback__isnull=True) | Q(admin_feedback='') | Q(admin_feedback_by__isnull=True) | Q(admin_feedback_by='')).filter(res_name=res_name.res_name)
        data={'feedback':feedback}
        return render(request,'Check_feedback.html',data)
    else:
        return redirect('error')

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
    
def create_food(request):
    if request.method=="POST":
        try:
            storage=messages.get_messages(request)
            storage.used=True
            food_by=request.POST['food_by']
            food_name=request.POST['food_name']
            food_description=request.POST['food_description']
            food_price=request.POST['food_price']
            food_photo=request.FILES['food_photo']
            Food.objects.create(food_name=food_name,food_description=food_description,food_price=food_price,food_picture=food_photo,food_by=food_by)
            messages.info(request,"New Food Item has been added")
            return redirect('add_food')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')

def create_delivery_partner(request):
    if request.method=='POST':
        try:
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            phno=request.POST['phno']
            address=request.POST['address']
            working_for=request.POST['working_for']
            storage=messages.get_messages(request)
            storage.used=True
            if Delivery_Person.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('add_delivery_partner')
            else:
                Delivery_Person.objects.create(del_name=name,email=email,password=password,mobile_number=phno,address=address,working_for=working_for)
                messages.info(request,"Delivery Partner added Successfully!")
                return redirect('add_delivery_partner')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')