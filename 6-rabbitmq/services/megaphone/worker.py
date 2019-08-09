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

import sys
import requests

from celery import Celery

sys.path.append('/etc/app/config')

celery = Celery('tasks')
celery.config_from_object('celeryconfig')
celery.conf.task_default_queue = 'megaphone'


@celery.task(name='megaphone')
def megaphone(listing_id):
    listing = requests.get('http://listings/listing_id').text
    return f'Megaphone for listing {listing} done'
