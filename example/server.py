
import http.server
import socketserver
import requests
from bs4 import BeautifulSoup

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
    soup = BeautifulSoup(req.text, "lxml")
    print(soup.title.string)
    httpd.serve_forever()

