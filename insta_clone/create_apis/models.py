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
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name = 'profile')
    profile_pic_url = models.ImageField(upload_to='profile_pic/', blank=True)
    
    bio = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=True)
