
try:
    import googleclouddebugger

    googleclouddebugger.enable(
        module='listings',
        version='0.0.1',
        service_account_json_file='/etc/app/secrets/gcp-service-account.json'
    )
except BaseException as e:
    print('ERROR!!!!!!!!', e)

from flask import Flask, abort
from pymongo import MongoClient
from bson import ObjectId
import pprint
import sys

from celery import Celery

sys.path.append('/etc/app/config')

app = Flask(__name__)
client = MongoClient('listings-db')
db = client.listings

celery = Celery('tasks')
celery.config_from_object('celeryconfig')
celery.conf.task_default_queue = 'megaphone'


@app.route('/')
def hello_world():
    return "Hello from listings service!\n"


@app.route('/all')
def listings_get():
    return pprint.pformat(list(db.listings.find()))


@app.route('/create/<title>')
def listings_create(title):
    result = db.listings.insert_one({'name': title})
    return str(result.inserted_id)


@app.route('/get/<id_>')
def get_by_id(id_):
    result = db.listings.find_one({'_id': ObjectId(id_)})
    if not result:
        abort(404)

    return str(result)


@app.route('/megaphone/<id_>')
def megaphone(id_):
    task = celery.send_task('megaphone', args=[id_])
    return f'task created. task id: {task.id}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
