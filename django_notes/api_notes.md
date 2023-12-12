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
