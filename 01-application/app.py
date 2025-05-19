import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR', 'Не указан')

    return f"""
    <html>
        <head><title>Информация о Хосте</title></head>
        <body>
            <h1>Информация о Хосте</h1>
            <p><strong>Имя хоста:</strong> {hostname}</p>
            <p><strong>IP адрес хоста:</strong> {ip_address}</p>
            <p><strong>Имя автора:</strong> {author}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
