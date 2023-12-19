from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile

class UserCreateSerializer(ModelSerializer):
    
    def create(self, validate_data):
        validate_data["password"] = make_password(validate_data["password"])    # hashing the password
        user = User.objects.create(**validate_data)   # passing validate_data dictionary as kwargs
        UserProfile.objects.create(user=user)   # creating UserProfile model
        return user
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email', )
        
        # fields, include, exclude
        
class UserViewSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'date_joined', )        
        
class UserProfileViewSerializer(ModelSerializer):
    
    user = UserViewSerializer()     # this object creates a json inside the outer json
    
    class Meta:
        model = UserProfile
        # this will give all the field except what is excluded
        exclude = ('is_verified',)
        