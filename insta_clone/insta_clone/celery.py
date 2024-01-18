import os
from celery import Celery

# Celery will need Django settings, in order to instantiate django app, to use models from the app in celery tasks.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insta_clone.settings')

# it will either look for this url in settings.py or use the url mentioned below as 2nd parameter
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

# this is an instance of celery library called an application (app for short). It is thread safe, so that multiple such
# instances with different configurations, components(workers, broker, etc) and tasks can co-exist together in the same process.
app = Celery('instaclone_celery')

# this is telling to look into settings.py for celery settings under namespace CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery will scan django projects for tasks.py and will register all the tasks (functions and methods that will run asynchronously)
app.autodiscover_tasks()


# redis server url, This broker acts as messaging queue that facilitates the communication between celery application and its workers.
app.conf.broker_url = BASE_REDIS_URL

# Configuring Celery beat, which is a schedular for periodic tasks. This scheduler stores scheduled task information into the database.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
