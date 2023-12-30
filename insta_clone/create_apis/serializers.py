from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile, NetworkEdge
from rest_framework import serializers

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
        
class UserProfileUpdateSerializer(ModelSerializer):
    
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    
    def update(self, instance, validated_data):
        # instance is the model of which the serializer is being saved, userprofile in this case
        user_model = instance.user   # since userprofile has a user field (OneOnOne field)
        user_model.first_name = validated_data.pop('first_name', None)
        user_model.last_name = validated_data.pop('last_name', None)
        user_model.save()
        
        instance.bio = validated_data.get("bio", None)
        # print(validated_data.get("profile_pic_url", None))
        instance.profile_pic_url = validated_data.get("profile_pic_url", None)
        instance.save()
        return instance
    
    class Meta:
        model = UserProfile
        # first_name and last_name are not with UserProfile model
        fields = ('first_name', 'last_name', 'bio', 'profile_pic_url', )
        
class NetworkEdgeSerializer(ModelSerializer):
    # from_user = UserProfileViewSerializer()
    # to_user = UserProfileViewSerializer()
    class Meta:
        model = NetworkEdge
        fields = ("from_user", "to_user", )


class NetworkEdgeFollowersSerializer(ModelSerializer):
    
    from_user = UserProfileViewSerializer()
    class Meta:
        model = NetworkEdge
        fields = ("from_user", )
        
        
class NetworkEdgeFollowingsSerializer(ModelSerializer):
    
    to_user = UserProfileViewSerializer()
    class Meta:
        model = NetworkEdge
        fields = ("to_user", )
