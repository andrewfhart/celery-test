from __future__ import absolute_import

from celery import Celery
import proj.celeryconfig as config

celery = Celery('proj.celery_main',
                broker=config.BROKER_URL,
                backend=config.CELERY_RESULT_BACKEND,
                include=['proj.tasks'])
                
# Optional configuration
celery.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    celery.start()
