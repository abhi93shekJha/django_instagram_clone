### Important points when creating Rest APIs using Django
- django.contrib.auth.models have User class.
- This class has all the fields and contraints defined by django.
- Very useful to use directly and then customise for personal use.
```python
class Meta:
    abstract = True
```
- Adding above line makes the outer class abstract for django models.
- This tells django to not include this class when creating tables out of models (when migrating).

### ModelSerializer
- A class that helps us remove code, "to take post data from request object, create a model field using that data and save the model".
- Simply put, it is an easy way to save coming request json data to table (first converting it to model) and vice-versa(converting model object to json when sending back the response).
- We create a serializers.py and create Serializer classes for the models to be used. Shown in the codebase.
- We will have to add only few lines of code in views.py to convert request data to respective model class, validate the data and save the data. It also helps create error object by itself. Shown in the codebase.
- We should always save hashed password to the database.
- When we do serializer_object.save() after serializer_object.is_valid(), then create(self, validate_data) method of Subclass of ModelSerializer class is called, which we can override to modify model's data before saving it to db. See in codebase.
- We can use a json inside a json, by keeping a serializer inside a serializer shown in the code below.
```python
from rest_framework.serializers import ModelSerializer
class UserViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'date_joined', )

class UserProfileViewSerializer(ModelSerializer):
    user = UserViewSerializer()   # this line creates an inside json
    class Meta:
        model = UserProfile
        # this will give all the field except what is excluded
        exclude = ('is_verified',)

# the field's name should be same when passing in request payload. It is same as created in Model :)
```

### Authentication vs Authorization
- Authentication is verification of a user when entering a system (ex. login).
- Authorization is verification of what resources and apps a user is authorised to use.

## More Important points:
### Path parameter example - http://localhost:8000/users/1
- We generally use filters with path parameters (Ex. http://localhost:8000/users/1/?is_active=True).
- Path parameter is mentioned in urls.py as below:
- path("<int:id>/<int:year>/", views.get_userid_with_year)
- Above pattern will match with "http://localhost:8000/users/1/1993/" not with "http://localhost:8000/users/1/1993"
- There are multiple converter types available, ex-<int:id>, <name> (if type not specified, it is string), <slug:slug> etc. (slug is "123abc-def-ghe_", alphnumeric strings with hyphons and underscores) 
- We can write views with path parameter as below:
```python
@api_view(['GET'])
def get_user(request, pk=None):
    # We should always use filter, instead of get, as get will throw exception if row not found or multiple rows found.
    user = UserProfile.objects.filter(id=pk).first()
    # if row does not exist, first() will return None
```
- Query parameter example - http://localhost:8000/users/get/?id=1

### Updating with DRF
- There is no need to pass in the id of the user to be updated in the url, because when access token is sent, the received request object gets a user variable. (request.user)
- Serialization- To convert an existing model object to json using a serializer. ('instance' is used in serializer constructor)
- Deserialization - To convert a request data back to serializer and finally save or update the data ('data' argument is used in serializer constructor.)
- Imp: So for updating, we use both 'data' and 'instance' arguements. 'data' for updating and 'instance' for  creating json of the updated row to send it back in response.
- update() method is overidden in writing Serializer class. We receive instance object and validated_data dictionary. Look at "UserProfileUpdateSerializer" serializer class in code.
- update() is called when the serializer is saved (save()) after validation (is_valid()).
- We can create fields inside serializer even if the fields are not present in the Model linked with serializer. See code for more understanding. (we user serializers.Charfield (from rest_framework import serializers)
- A code snippet relate to model below:
```python
class UserProfile(AbstractTimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name = 'profile')
# above code 'related_name' field will add a profile object inside the User model. It's like both the tables UserProfile and User have id of each other.
```
### Difference between PUT and POST
- POST is used for creating rows, PUT is used for updating existing rows/or creating if the row does not exists.
- The request payload for POST generally contains only data that needs to be created, where for PUT all the data is sent along with the updated field.
- PATCH is also for updation but only updated data is sent unlike PUT where all the data is sent in request payload.
- PUT is idempotent, meaning multiple requests with same payload should produce only one result, where POST creates multiple results.
- All the above things have to be implemented using logic, these are only conventions that are followed at all the places. Meaning it is not logically incorrect to both update using POST and create using POST but not accepted conventionally.
### GET and DELETE
- Similarly GET is used for read only single or multiple rows. Multiple requests should return same results (idempotancy).
- DELETE should always delete a row.
### Steps to update profile pic
- In settings.py of the project add (MEDIA_ROOT = BASE_DIR / 'media' and MEDIA_URL = '')
- Create an empty folder 'media' in the project root directory (similar to 'staticfiles' folder).
- Use ImageField in model. Specify upload_to arguement, it contains path inside MEDIA_ROOT to save the images.
- Install pillow using "pip install pillow". Django uses pillow internally (for ImageField actually).
