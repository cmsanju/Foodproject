from django.shortcuts import render,redirect
from Delivery.models import Delivery_Person
from Restaurant.models import Order

# Create your views here.
def delivery_home(request):
    email=request.session.get('email')
    if request.session and Delivery_Person.objects.filter(email=email).exists():
        obj=Delivery_Person.objects.get(email=email)
        orders=Order.objects.filter(del_id=obj.del_id)
        data={'obj':obj.del_name,'orders':orders}
        return render(request,'Delivery_home.html',data)
    else:
        return redirect('error')

#REST APIs
def change_status(request):
    if request.method=='POST':
        try:
            order_id=request.POST['order_id']
            order_status=request.POST['order_status']
            obj=Order.objects.get(order_id=order_id)
            obj.order_status=order_status
            obj.save()
            return redirect('delivery_home')
        except:
            return redirect('something_went_wrong')
    else:
        return redirect('error')