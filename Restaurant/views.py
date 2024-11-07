from django.shortcuts import render
from django.views import View

# Create your views here.
def res_registration(request):
    return render(request,'Restaurant_register.html')

def res_home(request):
    return render(request,'Restaurant_home.html')

def add_food(request):
    return render(request,'Add_food.html')

def view_orders(request):
    return render(request,'View_orders.html')

def add_delivery_partner(request):
    return render(request,'Add_delivery_partner.html')

def check_feedback(request):
    return render(request,'Check_feedback.html')