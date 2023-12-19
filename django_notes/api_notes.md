### Important points when creating Rest APIs using Django
- django.contrib.auth.models have User class.
- This class has all the fields and contraints defined by django.
- Very useful to use directly and then customise for personal use.
```python
class Meta:
    abstract = True
```
- Adding above line makes the outer class abstract for django models.
- This tells django to not include this class when creating tables out of models.

### ModelSerializer
- A class that helps us remove code, "to take post data from request object, create a model field using that data and save the model".
- We create a serializers.py and create Serializer classes for the models to be used. Shown in the codebase.
- We will have to add only few lines of code in views.py to convert request data to respective model class, validate the data and save the data. It also helps create error object by itself. Shown in the codebase.
- We should always save hashed password to the database.
- When we do serializer_object.save() after serializer_object.is_valid(), then create(self, validate_data) method of Subclass of ModelSerializer class is called, which we can override to modify model's data before saving it to db. See in codebase.

### Authentication vs Authorization
- Authentication is verification of a user when entering a system (ex. login).
- Authorization is verification of what resources and apps a user is authorised to use.

