### Framework:
- Framwork provides with boilerplate code. Analogy to a framework is already made flat having tap water, geyser, electricity connections, etc.
- Boilerplate code is the code that is already existing. It is already present to tackle some commonly occuring problems.
- Example - Ease with database connectivity, easy handling of request response cycle, help with user authentication.
- A framework can also be manipulated but should be done by an expert.
### Library:
- These are the astract code that a framework keeps to expose it's functionality via an API.
### API:
- Application programming interface. Provides an interface for a user to use.
- It lets a user use the functionalities of a framework, kept as library, in a controlled manner.
- Easy example for an API would be, an exposed public method, that has multiple private methods hidden from user.
### MVT
- Django is a Model, View and Template framework.
- Model keeps data to interact with database.
- View is where business logic is kept.
- Template is the interface a user looks at.
![Example Image](Django_MVT.png)
- In many other frameworks, Template is referred as View and View is referred as Controller.

### Localhost and Port (python manage.py runserver [port_number])
- Localhost is IP address of own computer. It is 127.0.0.1, which refers to the current machine.
- Port number is assigned for specific type of communication we are doing.
- Ex- Port 80 in case of web traffic. Port 443 in case of secure web traffic (HTTPS).

### Apps in Django  (python manage.py startapp your_app_name)
- Django provides us with the feature of dividing the entire projects into smaller apps.
- These apps are self contained (i.e. able to independently handle a functionality in a complex project).
- It helps in keeping a big project into small modules making managing and fixing easy.
- We can test them separately.
- A group of resources can work on an app independently in a large project.
- We can reuse the same app in a different project. Ex- An authentication system can be reused.
- We can customize an existing specific app.

### Models in Django (python manage.py makemigrations [your_app_name])  (python manage.py migrate)  (python manage.py shell)
- We use Django ORM to interact with databases.
- ORM - Object-Relational Mapping. It provides a way for developers to interact with any database using Python language.
- So, if it is mysql or postgres, we will have to use same syntax to interact with the database.
- It improves the development time.
- It takes care of almost all the CRUD cases. However, for executing complex queries we may have to write the query itself.
- Joins become really easy using class objects using shell (Django ORM provides interactive command line interface (shell) to perform CRUD to the tables using objects and methods, it is very much developer friendly).
- When doing migrate using (python manage.py migrate), Django checks for the models that are newly created with the existing tables, if the model not present as table, it creates new tables under the hood.
- Django performs all the queries under the hood hidden from us providing us a clean interface using ORM.
- We have to add the app name into 'INSTALLED_APPS' to use models.
```shell
from app_name.models import User, UserProfile
user = User()
user.name = "Abhishek"    # Add value
user.save()    # save value to a row

user_profile = UserProfile(bio = "Aiming from becoming a good developer", user=user)   # using
user_profile.save()

# get value out of table
user_list = User.objects.all()   # <QuerySet [<User: User object (1)>, <User: User object (2)>]>
# user_list acts as a list
for user in user_list:
   print(user.name)

# to get out rows that are certainly there, otherwise throws an exception (even when there are multiple rows found, it throws an exception)
user_obj = User.objects.get(pk=1)   # pk is automatically created
print(user_obj.name)   # prints "Abhishek"

# use filter always, do not throw execption. It ruturns multiple objects
# exists() method for checking if the row exists, or len() for same case. exist() is faster.
User.objects.filter()   # gives all the rows
User.objects.filter(pk=1)  # give one row
User.objects.filter(pk=1).exists()  # True or False
len(User.objects.filter(pk=1))   # returns 1

# We can also chain filters
user_objects = User.objects.filter(email='').filter(phone_number='')

# very easy to get foreign rows using Django ORM, join queries in sql are difficult to write
profiles = UserProfile.objects.all()
print(profiles[0].user.name)   # prints, "Abhishek"
```
