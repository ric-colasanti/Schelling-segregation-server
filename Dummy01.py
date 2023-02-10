from flask import Flask, render_template, request
from flask_socketio import SocketIO
from random import random
from threading import Lock

thread = None
thread_lock = Lock()
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


def background_thread():
    while True:
        socketio.emit('data', random())
        socketio.sleep(0.1)

@app.route('/')
def index():
    return render_template('Dummy01.html')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data,request.sid)
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

@socketio.on('connect')
def connect():
   print(request.sid)

@socketio.on('disconnect')
def disconnect():
    print(request.sid)

if __name__ == '__main__':
    socketio.run(app)