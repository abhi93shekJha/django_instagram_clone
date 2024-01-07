- We are adding below code for default settings for pagination provided by django.
```python
# in project's settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2
}
```
- Provides us two query parameters.
- Example - http://127.0.0.1:8000/post/?offset=0&limit=1
- offset is from where to start, and limit is how many results we want.
