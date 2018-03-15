from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('topper')

app.config_from_object('topper.celeryconfig')