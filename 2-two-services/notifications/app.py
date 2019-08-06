from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello from notifications service!\n"

@app.route('/request-listings')
def request_listings():
    return requests.get('http://listings/').text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
