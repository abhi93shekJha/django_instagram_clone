from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name="register_api"),
    
    # - Header of the request is "Authorization: Bearer access_token"
    path('get_all_user/', views.get_all_users, name="all_user_api"),
    
    # get a single use using id
    # path parameter
    path('user/<int:id>/', views.get_user, name="get_user"),
    
    # for updating existing user
    path('update_profile/', views.update_profile, name="update_profile"),
    
    path('<int:id>/', views.UserProfileDetail.as_view(), name="user_profile_detail")
]

