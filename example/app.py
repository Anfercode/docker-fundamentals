import requests
import os
from flask import Flask, render_template
from bs4 import BeautifulSoup

PORT = os.environ.get('port')
HOST = os.environ.get('host')
app = Flask(__name__, template_folder='')

@app.route('/')
def index():
    req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
    soup = BeautifulSoup(req.text, "lxml")
    return render_template('index.html', title=soup.title.string, port = PORT)

if __name__ == '__main__':
    app.run(debug=True, port=PORT, host=HOST)