from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

# # We can create custom Config class and have this app inherit these settings
# class MyCustomConfig(AppConfig):
#     default = True   # this will make django use this configuration file
#     # this can have multiple configurations regarding app, to be discussed later