from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

app = Celery('topper', broker='redis://localhost:6379/0', include=['topper.tasks'])