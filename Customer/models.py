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
    
class Customer(models.Model):
    cust_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    profile_picture=models.ImageField(upload_to='profile_picture/',validators=[validate_image])
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    mobile_number=models.BigIntegerField(unique=True)
    address=models.CharField(max_length=300)

class Feedback(models.Model):
    feed_id=models.AutoField(primary_key=True)
    res_name=models.CharField(max_length=100)
    rating=models.IntegerField()
    cust_feedback=models.CharField(max_length=200)
    cust_feedback_by=models.EmailField()
    admin_feedback=models.CharField(max_length=200)
    admin_feedback_by=models.EmailField()
