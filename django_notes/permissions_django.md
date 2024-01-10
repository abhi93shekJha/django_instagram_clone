### Authentication:
- User login logout, and user session. Can be implemented using JWT(Json Web Token) authentication mechanism.
### Authorisation:
- Django provides us a way to authenticate a user, whether he/she should be allowed to act on or access a resource.
- Custom permissions in django can be used to implement authorisation.
- An authorization permission is set using "IsAuthorized" that makes it mandatory for client to
- request using token in header for accessing or action on a resource.
- There is a need to call self.check_object_permissions(request, obj) if using class based views (by subclassing APIView),
- When using generic views, it is called implicitly in get_object method.
- It is written because a different user should not be allowed to delete the post or comment of a different user.
- Although user interface won't allow it, but it should also not be done from API.
- Below is the code for creating custom permission on object,
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
        
        if request.method in permissions.SAFE_METHODS:   # SAVE_METHODS are read only method, GET etc.
            return True
        
        return obj.author == request.user.profile       # custom logic to perform UPDATE,And DELETE only to the objects belonging to a particular user.

 
```
