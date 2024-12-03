from flask import Flask
import socket
import platform
import os

app = Flask(__name__)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
    return f'Welcome to Solanki Final Test API Server\nHostname: {hostname}\nIP: {ip_address}'
  
@app.route('/host')
def host_name():
    return {
        'hostname': hostname,
        'platform': platform.platform(),
        'python_version': platform.python_version()
    }

@app.route('/ip')
def host_ip():
    return {
        'ip_address': ip_address,
        'container_id': os.getenv('HOSTNAME', 'Unknown')
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
