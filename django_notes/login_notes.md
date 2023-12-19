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
- To now add login endpoint, we will have to simply add only below lines in project's urls.py.
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
