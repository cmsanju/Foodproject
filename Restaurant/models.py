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
    restaurant_picture=models.ImageField(upload_to='res_picture/',validators=[validate_image],default='static/res_home.jpg')
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    mobile_number=models.BigIntegerField(unique=True)
    address=models.CharField(max_length=300)