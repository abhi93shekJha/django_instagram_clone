### Authentication:
- User login logout, and user session. Can be implemented using JWT(Json Web Token) authentication mechanism.
### Authorisation:
- Django provides us a way to authorize a user, whether he/she should be allowed to act on or access a resource.
- Custom permissions in django can be used to implement authorization.
- An authorization permission is set using "IsAuthorized" that makes it mandatory for client to
- request using token in header for accessing or action on a resource.
- There is a need to call self.check_object_permissions(request, obj) in order to run permission logic(implemented below) if using class based views (by subclassing APIView),
- When using GenericViews, it is called implicitly in get_object method (no need for us to call).
- It is implemented so that a different user is not allowed to delete the post or comment of an another user.
- Although user interface won't allow it, but it should also not be done from API (using postman etc.).
- Below is the code for applying custom permission when modifying an object,
```python
# create permissions.py inside your_app directory
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    # this method runs at the view level, just before has_object_permission 
    def has_permission(self, request, view):
        # Check if the user has a specific role
        return request.user.is_authenticated and request.user.is_staff

    # this method is used for specifying object level permissions.
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:   # SAVE_METHODS are read only methods, GET etc.
            return True
        
        return obj.author == request.user.profile       # custom logic to perform UPDATE,And DELETE only to the objects belonging to a particular user.

 
```
