from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer, UserProfileViewSerializer, UserProfileUpdateSerializer, NetworkEdgeSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserProfile, NetworkEdge
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics, mixins

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


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request, id=None):
    
    user_profile = UserProfile.objects.filter(id=id).first()
    
    response_data = {
        "data":None,
        "error":None
    }
    status_code = ""
    
    if user_profile:
        serializer = UserProfileViewSerializer(instance=user_profile)
        response_data["data"] = serializer.data
        status_code = status.HTTP_200_OK
    else:
        response_data['error'] = "User does not exist!!"   
        status_code = status.HTTP_404_NOT_FOUND
    
    return Response(response_data, status=status_code)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_profile(request):
    
    user_profile_serializer = UserProfileUpdateSerializer(data=request.data, instance=request.user.profile)
    
    response_data = {
        "data":None,
        "error":None
    }
    status_code = ""
    
    if user_profile_serializer.is_valid():
        # print(user_profile_serializer.data)
        # the below line will call the update method in serializer.
        user_profile = user_profile_serializer.save()
        response_data["data"] = UserProfileViewSerializer(instance=user_profile).data
        status_code = status.HTTP_200_OK
    else:
        response_data["error"] = user_profile_serializer.errors
        status_code = status.HTTP_404_NOT_FOUND
    
    return Response(response_data, status_code)


class UserProfileDetail(APIView):
    
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]
    
    def get(self, request, id):
        
        user_profile = UserProfile.objects.filter(id=id).first()
    
        response_data = {
            "data":None,
            "error":None
        }
        status_code = ""
        
        if user_profile:
            serializer = UserProfileViewSerializer(instance=user_profile)
            response_data["data"] = serializer.data
            status_code = status.HTTP_200_OK
        else:
            response_data['error'] = "User does not exist!!"   
            status_code = status.HTTP_404_NOT_FOUND
        
        return Response(response_data, status=status_code)
    
    
    def post(self, request, id):
        
        user_profile_serializer = UserProfileUpdateSerializer(data=request.data, instance=request.user.profile)
    
        response_data = {
            "data":None,
            "error":None
        }
        status_code = ""
        
        if user_profile_serializer.is_valid():
            # print(user_profile_serializer.data)
            # the below line will call the update method in serializer.
            user_profile = user_profile_serializer.save()
            response_data["data"] = UserProfileViewSerializer(instance=user_profile).data
            status_code = status.HTTP_200_OK
        else:
            response_data["error"] = user_profile_serializer.errors
            status_code = status.HTTP_404_NOT_FOUND
        
        return Response(response_data, status_code)
        
    
    def delete(self, request, id):
        
        user = User.objects.filter(id=id)
        user.delete()
        
        response = {
            "data":None,
            "message": "User data deleted successfully!!"
        }
        
        return Response(response, status=status.HTTP_200_OK)


class UserNetworkEdgeView(mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = NetworkEdge.objects.all()    # this is the model we will be dealing with only
    serializer_class = NetworkEdgeSerializer    # and the serializer we are suppose be deal with only
    
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]
    
    def get(self, request):
        pass
    
    # below post will simply create and save a network model    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request):
        pass
    
    