from django.urls import path
from . import views

#  http://127.0.0.1:8000/users/index
#  http://127.0.0.1:8000/index
#  http://127.0.0.1:8000/users

urlpatterns = [
    # we are passing view.index function as a parameter
    # we are giving name to this url to be used later
    # for request  http://127.0.0.1:8000/users/index
    path('index/', views.index, name="users_main_view"),
    
    # for request, http://127.0.0.1:8000/users
    # path('', views.index, name="users_main_view")
    
    # use the below url to see registored list of users
    path('home/', views.home_page, name="users_home_page"),
    
    # use this url to go to registor page
    path('register/', views.register, name="users_registration")
]


