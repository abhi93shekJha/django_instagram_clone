### Steps to implememnt token based login in Django using JSON Web Token Authentication (JWT Authentication)
- pip install djangorestframework-simplejwt
- Either add in project's settings.py, this way we will have to make all the requests from client essentially send token in header.
- Or we can add it as decorator for view's methods, which gives us flexibility to select only required view to receive token in header. (Preferred)
- As soon as a user signs up, we will send him/her refresh token and access token as response from the server.
```python
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
```
- As a next step, we have to append the below code in project's urls.py
- This urls gives us access token in response to refresh token.
```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```
- Now below code is added in project's urls.py. This verifies if the token sent by client is valid.
```python
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    ...
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ...
]
```
- To now add login endpoint, we will have to simply add only below line in project's urls.py.
- Note here this is possible because we used the User Model provided by djang.contrib.auth.models package.
- This links our login api to the same User model under the hood.
- It accepts username and password and sends back refresh token and access token in response to be sent as header in subsequent apis.
```python
urlpatterns = [
    ...
    path('login/', TokenObtainPairView.as_view(), name='login_api'),
    ...
]
```
- Code to add decorators and their importance to make it mandatory for an api to send token in header
- Header of the request is "Authorization: Bearer access_token"
```python
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([JWTAuthentication])   # enables authentication of the user, fills the request.user variable (Anonymous if token not send, otherwise username associated with the user)
@permission_classes([IsAuthenticated])    # makes it mandatory for an api to send token in header

def get_all_users(request):
    all_profile = UserProfile.objects.all()
    
    print("User name: - " + str(request.user))
    
    # converts it back to json
    user_profile_serializer = UserViewSerializer(instance=all_profile, many=True)
    
    return Response(user_profile_serializer.data, status=status.HTTP_200_OK)
```
- We can add settings to set how much time refresh and access tokens should be valid. See the below code,
- Client will have to get new access token to make server request at every 5 minutes using the refresh token with the below settings. 
```python
from datetime import timedelta
if DEBUG:
    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    }
```
