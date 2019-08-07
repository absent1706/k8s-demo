from flask import Flask
from pymongo import MongoClient
import pprint

app = Flask(__name__)
client = MongoClient('listings-db')
db = client.listings

@app.route('/')
def hello_world():
    return "Hello from listings service!\n"

@app.route('/listings')
def listings_get():
    return pprint.pformat(list(db.listings.find()))

@app.route('/listings/create/<title>')
def listings_create(title):
    result = db.listings.insert_one({'name': title})
    return str(result.inserted_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
