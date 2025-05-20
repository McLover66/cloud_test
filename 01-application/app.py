import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR', 'Не указан')

    return {
        "hostname": hostname,
        "ip address": ip_address,
        "author": author
    } 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
