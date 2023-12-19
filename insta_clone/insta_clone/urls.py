"""
URL configuration for insta_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

# Always use '/' after url name(not before), if used anywhere else it may have consequences later
# Django goes to the list of urlpatterns one by one for searching and enters into the apps urls in the same sequence
urlpatterns = [
    path('admin/', admin.site.urls),
    # the below line will append the BASE_DIR from setting.py and use the path to go to users.urls file.
    path('users/', include('users.urls')),
    # for request http://127.0.0.1:8000, to move to users.urls
    # path('', include('users.urls'))
    path('apis/', include('create_apis.urls')),
    
    # this url gives access token from refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # we are adding this line of code verify the access token sent by client
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # to create login api, we only need to add this line. It is using the User object by django.contrib.auth.models under the hood
    # It expects username and password and sends back refresh token and access token
    path('login/', TokenObtainPairView.as_view(), name='login_api'),
]
