from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def say_snippets(snippet):
    return f'The snippets is: {snippet}'