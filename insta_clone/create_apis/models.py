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
    
    
class NetworkEdge(AbstractTimeStamp):
    
    from_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name = "followings")
    
    to_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name = "followers") 
        
# Example below
# from_user  to_user
#   1          3
#   1          2
#   1          4
#   2          4
# for user with userid 1, 
#   user.followings.all() will give,   
#   from_user  to_user
#   1          3
#   1          2
#   1          4
# it is basically giving all the users that current user(id=1) is following, which are 3, 2 and 4.

# for user with userid 2, 
#   user.followers.all() will give,
#   from_user  to_user
#   1          2
# it is basically giving all the followers of current user (id=2), which is 1.