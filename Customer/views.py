from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.views import View
from Customer.models import Customer,Feedback,Cart
from Restaurant.models import Food, Restaurant, Order
from Delivery.models import Delivery_Person

from django.contrib import messages
from datetime import datetime

# Create your views here.
def home(request):
    restaurant=Restaurant.objects.order_by('?')[:4]
    return render(request,'Home.html',{'data':restaurant})

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
        restaurant=Restaurant.objects.all()
        data={'cus_name':customer,'restaurant':restaurant}
        return render(request,'Customer_home.html',data)
    else:
        return redirect('error')
    
def view_orders_cus(request):
    email=request.session.get('email')
    if request.session and Customer.objects.filter(email=email).exists():
        orders=Order.objects.filter(cust_email=email).exclude(order_status='Delivered')
        data=[]
        for order in orders:
            res=Restaurant.objects.get(res_id=order.res_id)
            if order.del_id!=0:
                delivery=Delivery_Person.objects.get(del_id=order.del_id)
                data.append({
                    'order_id':order.order_id,
                    'res_name':res.res_name,
                    'order_status':order.order_status,
                    'ordered_on':order.ordered_on,
                    'del_name':delivery.del_name,
                    'mobile_number':delivery.mobile_number,
                    'order_details':order.order_details,
                    'total_price':order.total_price,
                })
            else:
                data.append({
                    'order_id':order.order_id,
                    'res_name':res.res_name,
                    'order_status':order.order_status,
                    'ordered_on':order.ordered_on,
                    'order_details':order.order_details,
                    'total_price':order.total_price,
                })
        return render(request,'View_orders_cus.html',{'data':data})
    else:
        return redirect('error')

def feedback_cus(request):
    email=request.session.get('email')
    if request.session and Customer.objects.filter(email=email).exists():
        restaurants=Restaurant.objects.all()
        return render(request,'Feedback_cus.html',{'restaurants':restaurants,'email':email})
    else:
        return redirect('error')

def restaurant_menu(request,res_id):
    email=request.session.get('email')
    if request.session and Customer.objects.filter(email=email).exists():
        restaurant=Restaurant.objects.get(res_id=res_id)
        food=Food.objects.filter(food_by=restaurant.res_name)
        return render(request,'Customer_restaurant_menu.html',{'food':food,'email':email,'res_id':res_id,'cart':Cart.objects.filter(cust_email=email).exists()})
    else:
        return redirect('error')

def add_to_cart(request):
    """
    View to add an item to the cart.
    """
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        price = float(request.POST.get('price'))
        quantity = int(request.POST.get('quantity', 1))
        cust_email=request.POST.get('cust_email')
        res_id=int(request.POST.get('res_id'))
        print(res_id,type(res_id))
        # Check if the item is already in the cart
        if Cart.objects.filter(cust_email=cust_email).exists():
            restaurant=Cart.objects.filter(cust_email=cust_email).first()
            if restaurant.res_id==int(res_id):
                cart_item, created = Cart.objects.get_or_create(
                    cust_email=cust_email,
                    product_name=product_name,
                    res_id=res_id,
                    defaults={'price': price, 'quantity': quantity},   
                )

                if not created:
                    # Update quantity if item already exists
                    cart_item.quantity += quantity
                    cart_item.save()
                return JsonResponse({'message': 'Item added to cart successfully!'})
            else:
                return JsonResponse({'message':'Can not add item from different restaurants'})
        else:
            #restaurant=Cart.objects.filter(cust_email=cust_email).first()
            #if restaurant.res_id==int(res_id):
                print("else")
                cart_item, created = Cart.objects.get_or_create(
                    cust_email=cust_email,
                    product_name=product_name,
                    res_id=res_id,
                    defaults={'price': price, 'quantity': quantity},   
                )

                if not created:
                    # Update quantity if item already exists
                    cart_item.quantity += quantity
                    cart_item.save()
                return JsonResponse({'message': 'Item added to cart successfully!'})
            #else:
                #return JsonResponse({'message':'Can not add item from different restaurants'})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def cart_view(request):
    """
    View to display all items in the cart.
    """
    email=request.session.get('email')
    cart_items = Cart.objects.filter(cust_email=email)
    if cart_items:
        res_get_id=Cart.objects.filter(cust_email=email).first()
        customer=Customer.objects.get(email=email)
        cart_view=Cart.objects.filter(cust_email=email)
        order_details=""
        for x in cart_view:
            order_details+=str(x.quantity)+" x "+x.product_name+","
        order_details=order_details[:len(order_details)-1]
        total = sum(item.total_price for item in cart_items)
        return render(request, 'Order_cart.html', {'cart_items': cart_items, 'total': total,'customer':customer,'order_details':order_details,'res_id':res_get_id.res_id})
    else:
        return redirect('error')

def update_cart(request,id):
    """
    View to update the quantity of an item in the cart.
    """
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, id=id)
        new_quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity = new_quantity
        cart_item.save()

        return JsonResponse({'message': 'Cart updated successfully!', 'item_total': cart_item.total_price})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def remove_from_cart(request,id):
    """
    View to remove an item from the cart.
    """
    email=request.session.get('email')
    cart_item = Cart.objects.get(id=id,cust_email=email)
    cart_item.delete()

    return JsonResponse({'message': 'Item removed from cart!'})

def payment(request):
    return render(request,'Payment.html')

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
                if(Delivery_Person.objects.filter(email=email,password=password)):
                    request.session['email']=email
                    return redirect('delivery_home')
                else:
                    messages.info(request,"Username or password does not match")
                    return redirect('user_login')
            else:
                return redirect('/')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')
    
def create_feedback(request):
    if request.method=='POST':
        try:
            email=request.POST['email']
            restaurant=request.POST['restaurant']
            rating=request.POST['rating']
            feedback=request.POST['feedback']
            restaurants=Restaurant.objects.all()
            Feedback.objects.create(res_name=restaurant,rating=rating,cust_feedback=feedback,cust_feedback_by=email)
            return render(request,'Feedback_cus.html',{'message':"Feedback received successfully",'restaurants':restaurants,'email':email})
        except:
            return render(request,'Feedback_cus.html',{'message':"Some error occured"})
    else:
        return redirect('error')

def place_order(request):
    if request.method=='POST':
        #try:
            cust_email=request.POST['cust_email']
            cust_name=request.POST['cust_name']
            cust_address=request.POST['cust_address']
            order_details=request.POST['order_details']
            res_id=request.POST['res_id']
            total_price=request.POST['total_price']
            ordered_on=datetime.now()
            Order.objects.create(cust_email=cust_email,cust_name=cust_name,cust_address=cust_address,order_details=order_details,res_id=res_id,total_price=total_price,ordered_on=ordered_on)
            Cart.objects.filter(cust_email=cust_email,res_id=res_id).delete()
            return redirect('payment')
        #except:
            #return redirect('something_went_wrong')
    else:
        return redirect('error')