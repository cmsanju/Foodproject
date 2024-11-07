from django.db import models

# Create your models here.
class Restaurant(models.Model):
    res_id=models.AutoField(primary_key=True)
    res_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    mobile_number=models.BigIntegerField(unique=True)
    address=models.CharField(max_length=300)