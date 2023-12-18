from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# For below abstract class tables won't be created when migrating
class AbstractTimeStamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # this inner class makes the outer class abstract for Django
    class Meta:
        abstract=True

class UserProfile(AbstractTimeStamp):
    
    DEFAULT_PROFILE_PIC_URL = 'https://mywebsite.com/placeholder.png'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    profile_pic_url = models.CharField(max_length=255, default=DEFAULT_PROFILE_PIC_URL)
    
    bio = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=True)
