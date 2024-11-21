from django.db import models

# Create your models here.
class Delivery_Person(models.Model):
    del_id=models.AutoField(primary_key=True)
    del_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    mobile_number=models.BigIntegerField(unique=True)
    address=models.CharField(max_length=300)
    working_for=models.CharField(max_length=100,default='')