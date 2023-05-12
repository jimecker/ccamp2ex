from flask import Flask, request
import json
import socket

app = Flask(__name__)

storage = 0

@app.route('/',methods=['GET','POST'])
def process():
    if request.method == 'GET':
        name = socket.gethostname()
        return name

    if request.method == 'POST':
        subprocess.Popen()
        return ""

if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug = True)

