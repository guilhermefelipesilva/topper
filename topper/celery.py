from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from topper import celeryconfig

app = Celery('topper')

app.config_from_object(celeryconfig)

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
