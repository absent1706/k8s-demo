import os  
import time  
import random
from celery import Celery

celery = Celery('tasks')
celery.config_from_object('celeryconfig')

# The name parameter is the key here
@celery.task(name='mytasks.add')
def add(x, y):  
    if random.random() < 0.5:
        raise ValueError('TEST ERROR!!!!')
    time.sleep(5)  # lets sleep for a while before doing the gigantic addition task!
    return x + y
