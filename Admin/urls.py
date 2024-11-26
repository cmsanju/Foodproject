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
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('all_users/',views.all_users,name="all_users"),
    path('view_users/',views.view_users,name="view_users"),
    path('view_restaurants/',views.view_restaurants,name="view_restaurants"),
    path('view_feedback/',views.view_feedback,name="view_feedback"),
    path('total_orders/',views.total_orders,name="total_orders"),
    path('add_admin/',views.add_admin,name="add_admin"),

    # REST APIS
    path('admin_login_verification/',views.admin_login_verification,name="admin_login_verification"), 
    path('give_feedback/',views.give_feedback,name="give_feedback"),
    path('create_admin/',views.create_admin,name="create_admin"),
]
