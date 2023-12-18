from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer

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
        
        response_data["data"] = {
            "user_id":user.id
        }
        response_status = status.HTTP_201_CREATED
    else:
        response_data["errors"] = serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST
        
    
    return Response(response_data, status=status.HTTP_201_CREATED)