### There can be various functionalities that we may want to implement, in case of a social networking app as below,
- When someone follows a user, send push notification to the user. (email or push)
- When someone likes or comments on your post, send a push notification or email.
- When a post is uploaded, create multiple version of the image or video being uploaded, for different screens
and sizes.

The above tasks should happen asynchronously in near real time, and the actual task that a user is performing 
should not be hampered by the above tasks.
For example, if a user is creating post, modification of images should not happen linearly, as it may lead to 
failure of post creation. If it fails asynchronously(let's say we are making third party API call), 
we would have a way to restart the task.
- Celery helps achieve this.
- It is a task queue, with real time processing. It also does task scheduling.
- It helps in distributing tasks among multiple workers to process task parallely.
- It helps in processing tasks asynchronously.

Task Queue
- Client (django here) adds task to the task queue, and a broker is used to provide the task to workers (thread
or a machine).
- Celery system can consists of multiple brokers and workers allowing to scale horizontally.
- __Redis__ we are using as a broker for our use case. It will store celery tasks.
- Redis is an in momory database. It keeps data in key-value pair.
- It keeps the data in RAM and hence is extremely fast and used as Cache for achieving low latency.
- It can be used as a broker as well.
- It is designed to be used in distributed system allowing horizontal scaling.

### Installation of Celery and Redis
- pip install celery
- pip install django-celery-beat , celery beat is used to schedule task. We can set a time for task scheduling
and it will be performed after specified time interval. celery beat gives the task to workers to perform
asynchronously. Implemented here????.
- pip install django-celery-results , helps save the result from celery to database.
- pip install redis

### Steps to implement Celery with Reddis
- Add 'django_celery_beat', django_celery_results' in INSTALLED_APPS in settings.py of project.
- Run migrations. This will create few new tables in DB.
- Now we will install Redis and store our celery tasks there.
- Start Redis server.
- Create celery.py in project module.
- Celery will need Django settings, in order to instantiate django app, to use models from the app in celery tasks.
- Implementing the above info in celery.py at line 4.
- Rest of the celery configurations are present and explained here ????.
- Next we will create tasks.py in my application. We will write functions(tasks that will run asynchornously),
and annotate it with @app.task(name="task_name").
- We can have multiple parameters inside task function, such as, Task.name, Task.request, Task.max_tries etc.
- Add a configuration in settings.py i.e. CELERY_RESULT_BACKEND = 'django-db'.
- Command to run celery - celery -A(name of project) insta_clone worker(the actual task we will be executing) -l(level of logging) info/warning/debug -f(where celery logs should be stored) celery.logs
- When running the function as task_function.delay(), using shell, it will run asynchronously.
- Database django_celery_results_taskresult table gets filled by result and other informations.
- We should always restart the celery server, when updating or creating a task.
