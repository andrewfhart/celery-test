from celery import Celery

celery = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

@celery.task 
def add(x, y):
    return x + y
