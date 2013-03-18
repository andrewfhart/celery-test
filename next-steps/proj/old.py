from __future__ import absolute_import
from celery import Celery
#import proj.celeryconfig as config

celery = Celery('proj.celery',
                broker='redis://',
                backend='redis://',
                include=['proj.tasks'])
                
# Optional configuration
celery.conf.upadate(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    celery.start()
