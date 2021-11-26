from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# from celery.schedules import crontab

logger = logging.getLogger("Celery")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "universe_blog.settings")

app = Celery("universe_blog")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


# @app.task(bind=True)
# def debug_task(self):
#     print("Request: {0!r}".format(self.request))


REDIS_CONNECTION = "{protocol}://{username}:{password}@{host}:{port}".format(
    protocol=os.environ.get("REDIS_PROTOCOL", "redis"),
    username=os.environ.get("REDIS_USER", ""),
    password=os.environ.get("REDIS_PASSWORD", ""),
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=os.environ.get("REDIS_PORT", "6379"),
)

CELERY_CONFIG = dict(
    BROKER_URL="{redis}/0".format(redis=REDIS_CONNECTION),
    BROKER_TRANSPORT_OPTIONS={
        "visibility_timeout": 3600,
        "fanout_prefix": True,
        "fanout_patterns": True,
    },
    CELERYBEAT_SCHEDULER="django_celery_beat.schedulers:DatabaseScheduler",
    # CELERY_RESULT_BACKEND='{redis}/1'.format(redis=REDIS_CONNECTION),
    CELERY_DISABLE_RATE_LIMITS=True,
    CELERY_IGNORE_RESULT=True,
    CELERY_ACCEPT_CONTENT=["application/json"],
    CELERY_TASK_SERIALIZER="json",
    CELERY_RESULT_SERIALIZER="json",
)

app.conf.update(**CELERY_CONFIG)

app.conf.beat_schedule = {
    "send_fcm_notifications": {
        "task": "fcm.tasks.send_recurrent_messages",
        "schedule": crontab(
            minute="01", hour="6", day_of_month="*", month_of_year="*", day_of_week="*"
        ),
    },
}