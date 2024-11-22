from django.shortcuts import render,redirect
from Delivery.models import Delivery_Person

# Create your views here.
def delivery_home(request):
    email=request.session.get('email')
    if request.session and Delivery_Person.objects.filter(email=email).exists():
        obj=Delivery_Person.objects.get(email=email)
        data={'obj':obj.del_name}
        return render(request,'Delivery_home.html',data)
    else:
        return redirect('error')

#REST APIs