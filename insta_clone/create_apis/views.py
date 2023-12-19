from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer, UserProfileViewSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserProfile
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST'])
def register_user(request):
    
    serializer = UserCreateSerializer(data=request.data)
    
    response_data = {
        "errors":None,
        "data":None
    }
    
    if serializer.is_valid():
        # it calls the create method of UserCreateSerializer class
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        
        # access token to be appended in header in all subsequent client request.
        response_data["data"] = {
            "user_id":user.id,
            "refresh":str(refresh),
            'access': str(refresh.access_token),
        }
        response_status = status.HTTP_201_CREATED
    else:
        response_data["errors"] = serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST
        
    return Response(response_data, response_status)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])   # enables authentication of the user, fills the request.user variable (Anonymous if token not send, otherwise username associated with the user)
@permission_classes([IsAuthenticated])    # makes it mandatory for an api to send token in header

# - Header of the request is "Authorization: Bearer access_token"
def get_all_users(request):
    all_profile = UserProfile.objects.all()
    
    print("User name: - " + str(request.user))
    
    # converts it back to json
    user_profile_serializer = UserProfileViewSerializer(instance=all_profile, many=True)
    
    return Response(user_profile_serializer.data, status=status.HTTP_200_OK)
