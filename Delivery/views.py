from django.shortcuts import render

# Create your views here.
def delivery_home(request):
    return render(request,'Delivery_home.html')

#REST APIs