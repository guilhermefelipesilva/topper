from ..settings import *  # noqa


DEBUG = True

CELERY_BROKER_URL = os.environ.get('BROKER_URL', 'redis://localhost:6379/0')

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

CELERY_TIMEZONE = "America/Sao_Paulo"

CELERY_ENABLE_UTC = True
