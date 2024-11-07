from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.EmailField(unique=True)
    password=models.TextField(max_length=50)
