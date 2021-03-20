import os
from celery import Celery
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailytips.settings')
app = Celery('dailytips')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='')


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
# Executes every Monday morning at 7:30 a.m.
'run_testing': {
    # run this task every minute
    'task': 'tips.tasks.get_daily_tips',
    'schedule': crontab()
  },
}