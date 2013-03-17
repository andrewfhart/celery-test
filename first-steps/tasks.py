import celeryconfig as config
from celery import Celery

celery = Celery('tasks', backend=config.CELERY_RESULT_BACKEND, broker=config.BROKER_URL)

@celery.task 
def add(x, y):
    return x + y
