### What are we creating?
- A user can follow many people.
- Many people can follow a user.
- We are creating multiple apis to add followers for a user, get followers of a user, get list of what a user is following, delete follower of a user etc.
- You can think usecase of instagram application.
### Steps involved in the implementation:
- We have to make a manyToMany connection between UserProfile models, for that creating a separate model class "NetworkEdge" (just like a lookup table).
```python

class NetworkEdge(AbstractTimeStamp):
    from_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name = "followings")
    to_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name = "followers")

# Example below
# from_user  to_user
#   1          3
#   1          2
#   1          4
#   2          4
# for user with userid 1, 
#   user.followings.all() will give,   
#   from_user  to_user
#   1          3
#   1          2
#   1          4
# it is basically giving all the users that current user(id=1) is following, which are 3, 2 and 4.

# for user with userid 2, 
#   user.followers.all() will give,
#   from_user  to_user
#   1          2
# it is basically giving all the followers of current user (id=2), which is 1.
```
- __Important__:
- Here NetworkEdge has from_user and to_user UserProfile models as foreign keys.
- You can think of it as a lookup table.
- Just like we can get UserProfiles using NetworkEdge instance, related_name helps to refer back to NetworkEdge model using UserProfile instance.
- so, user_profile_model.followings.all() will give us all the NetworkEdge rows which user is following. With ".to_user" we can get all the followings.
- Similarly user_profile_model.followers.all() will give us all NetworkEdge rows which is following the user. With ".from_user" we can get all the followers.  
