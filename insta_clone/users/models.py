from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    # this field does automatic email validation
    email = models.EmailField(max_length=255, unique=True, null=False)
    
    phone_number = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=False)
    
    password = models.CharField(max_length=255, null=False, unique=True)
    
    # auto_now_add will fill DateTime value when this object gets created
    created_on = models.DateTimeField(auto_now_add=True)
    # auto_now will automatically fill the date time of the row creation
    updated_on = models.DateTimeField(auto_now=True)
    
class UserProfile(models.Model):
    
    DEFAULT_PROFILE_PIC_URL = 'https://mywebsite.com/placeholder.png'
    
    profile_pic_url = models.CharField(max_length=255, default=DEFAULT_PROFILE_PIC_URL)
    bio = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    