import requests
import os
from flask import Flask, render_template
from bs4 import BeautifulSoup
from pymongo import MongoClient

HOST = os.environ.get('host')
FLASK_PORT = os.environ.get('flask_port')
MONGO_URL = os.environ.get('mongo_url')

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
    soup = BeautifulSoup(req.text, "lxml")
    return render_template('index.html', title=soup.title.string, port = FLASK_PORT)

@app.route('/mongo-health-check')
def mongo_health_check():
    try:
        client = MongoClient(MONGO_URL)
        print(client.db.list_collection_names())
        return render_template('test_mongo.html')
    except Exception as error:
        return render_template('failed_connection.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, port=FLASK_PORT, host=HOST)