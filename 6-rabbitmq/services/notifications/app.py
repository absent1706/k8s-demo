try:
    import googleclouddebugger

    googleclouddebugger.enable(
        module='notifications',
        version='0.0.1',
        service_account_json_file='/etc/app/secrets/gcp-service-account.json'
    )
except BaseException as e:
    print('ERROR!!!!!!!!', e)

from flask import Flask
from pymongo import MongoClient
import requests
import pprint

app = Flask(__name__)
client = MongoClient('notifications-db')
db = client.notifications


@app.route('/request-listings')
def request_listings():
    return requests.get('http://listings/all').text


@app.route('/notifications')
def notifications_get():
    return pprint.pformat(list(db.notifications.find()))


@app.route('/notifications/create/<description>')
def notifications_create(description):
    result = db.notifications.insert_one({'description': description, 'user_id': 2})
    return str(result.inserted_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
