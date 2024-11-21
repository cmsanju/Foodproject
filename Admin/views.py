from django.shortcuts import render,redirect
from django.views import View
from Admin.models import Admin
from Customer.models import Customer,Feedback
from Restaurant.models import Restaurant

from django.contrib import messages
from django.db.models import Q
# Create your views here.
def admin_login(request):
    return render(request,'Admin_login.html')

def admin_home(request):
    email=request.session.get('email')
    if request.session and Admin.objects.filter(email=email).exists():
        cus_count=Customer.objects.all().count()
        fed_count=Feedback.objects.filter(Q(admin_feedback__isnull=True) | Q(admin_feedback__exact=''),Q(admin_feedback_by__isnull=True) | Q(admin_feedback_by__exact='')).count()
        res_count=Restaurant.objects.all().count()
        data={'cus_count':cus_count,'fed_count':fed_count,'res_count':res_count}
        return render(request,'Admin_home.html',data)
    else:
        return redirect('error')

def all_users(request):
    return render(request,'All_users.html')

def view_users(request):
    email=request.session.get('email')
    if request.session and Admin.objects.filter(email=email).exists():
        cus=Customer.objects.all()
        return render(request,'View_users.html',{'cus':cus})
    else:
        return redirect('error')
    
def view_restaurants(request):
    email=request.session.get('email')
    if request.session and Admin.objects.filter(email=email).exists():
        res=Restaurant.objects.all()
        return render(request,'View_restaurants.html',{'res':res})
    else:
        return redirect('error')
    
def view_feedback(request):
    email=request.session.get('email')
    if request.session and Admin.objects.filter(email=email).exists():
        fed=Feedback.objects.filter(Q(admin_feedback__isnull=True) | Q(admin_feedback__exact=''),Q(admin_feedback_by__isnull=True) | Q(admin_feedback_by__exact=''))
        return render(request,'View_feedback.html',{'fed':fed})
    else:
        return redirect('error')
    
def add_admin(request):
    email=request.session.get('email')
    if request.session and Admin.objects.filter(email=email).exists():
        return render(request,'Add_admin.html')
    else:
        return redirect('error')

# REST APIs
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
    
def give_feedback(request):
    if request.method=='POST':
        try:
            itemId=request.POST['itemId']
            reply=request.POST['reply']
            email=request.session.get('email')
            obj=Feedback.objects.get(feed_id=itemId)
            obj.admin_feedback=reply
            obj.admin_feedback_by=email
            obj.save()
            return redirect('/view_feedback/')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')

def create_admin(request):
    if request.method=="POST":
        try:    
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            storage=messages.get_messages(request)
            storage.used=True
            Admin.objects.create(name=name,email=email,password=password)
            messages.info(request,'New Admin Created Sucessfully!')
            return redirect('add_admin')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')