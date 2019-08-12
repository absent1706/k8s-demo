# try:
#     import googleclouddebugger
#
#     googleclouddebugger.enable(
#         module='megaphone',
#         version='0.0.1',
#         service_account_json_file='/etc/app/secrets/gcp-service-account.json'
#     )
# except BaseException as e:
#     print('ERROR!!!!!!!!', e)

import requests
import os

from celery import Celery

celery = Celery('tasks',
                broker=os.getenv('CELERY_BROKER_URL'),
                result=os.getenv('CELERY_RESULT_BACKEND'))
celery.conf.task_default_queue = 'megaphone'


@celery.task(name='megaphone')
def megaphone(listing_id):
    import time; time.sleep(5)
    import random
    if random.random() < 0.3:
        raise ValueError('Some test fail reason')
    listing = requests.get(f'http://listings/get/{listing_id}').text
    return f'Megaphone for listing {listing} done'
