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
    path('',views.home,name="home"),
    path('error/',views.error,name="error"),
    path('something_went_wrong/',views.something_went_wrong,name="something_went_wrong"),
    path('user_registration/',views.user_registration,name="user_registration"),
    path('user_login/',views.user_login,name="user_login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
    path('cus_home/',views.cus_home,name="cus_home"),
    path('my_profile/',views.my_profile,name="my_profile"),
    path('view_orders_cus/',views.view_orders_cus,name="view_orders_cus"),
    path('feedback_cus/',views.feedback_cus,name="feedback_cus"),
    path('restaurant_menu/<res_id>',views.restaurant_menu,name="restaurant_menu"),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/update/<int:id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment/',views.payment,name="payment"),

    # REST APIs 

    path('create_customer/',views.create_customer,name="create_customer"),
    path('login_verification/',views.login_verification,name="login_verification"),
    path('create_feedback/',views.create_feedback,name="create_feedback"),
    path('place_order/',views.place_order,name="place_order"),
]
