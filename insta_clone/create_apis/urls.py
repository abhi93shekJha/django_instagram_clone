from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name="register_api"),
    
    # - Header of the request is "Authorization: Bearer access_token"
    path('get_all_user', views.get_all_users, name="all_user_api"),
]

