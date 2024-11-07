"""
URL configuration for Foodproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('res_registration/',views.res_registration,name="res_registration"),
    path('res_home/',views.res_home,name="res_home"),
    path('add_food/',views.add_food,name="add_food"),
    path('view_orders/',views.view_orders,name="view_orders"),
    path('add_delivery_partner/',views.add_delivery_partner,name="add_delivery_partner"),
    path('check_feedback/',views.check_feedback,name="check_feedback"),
]
