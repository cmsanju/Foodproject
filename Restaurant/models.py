from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_image(file):
    valid_mime_types = ['image/jpeg', 'image/png', 'image/jpg',]
    file_mime_type = file.file.content_type
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Only .png, .jpg, and .jpeg files are allowed.')

    if file.size > 1 * 1024 * 1024:  # 1MB
        raise ValidationError('File size must be less than 1MB.')
    
class Restaurant(models.Model):
    res_id=models.AutoField(primary_key=True)
    res_name=models.CharField(max_length=100)
    restaurant_picture=models.ImageField(upload_to='res_picture/',validators=[validate_image],default='res_picture/res_home.jpg')
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    mobile_number=models.BigIntegerField(unique=True)
    address=models.CharField(max_length=300)

class Food(models.Model):
    food_id=models.AutoField(primary_key=True)
    food_name=models.CharField(max_length=100)
    food_description=models.CharField(max_length=300)
    food_price=models.IntegerField()
    food_picture=models.ImageField(upload_to="foods/",validators=[validate_image])
    food_by=models.CharField(max_length=100)

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    cust_email=models.EmailField()
    cust_name=models.CharField(max_length=100)
    cust_address=models.CharField(max_length=300)
    order_details=models.CharField(max_length=2000)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    res_id=models.BigIntegerField()
    del_id=models.BigIntegerField(default=0)
    order_status=models.CharField(max_length=15,default="Pending")
    ordered_on=models.DateTimeField()


