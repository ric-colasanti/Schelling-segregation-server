from flask import Flask, render_template, request
from flask_socketio import SocketIO,join_room, leave_room
from random import random
from schelling import Experiment

threads = []
users={}
count=0
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


def background_thread(user_id):
    experiment = Experiment(20)
    experiment.setUp(100)
    while True:
        experiment.iterate()
        sim, happy, unhappy = experiment.getResultMatrix()
        socketio.emit('data', [sim, happy, unhappy], to = user_id)
        socketio.sleep(.00001)

@app.route('/')
def index():
    return render_template('Dummy01.html')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data+ request.sid)
    global threads
    threads.append(socketio.start_background_task(background_thread(request.sid)))

@socketio.on('connect')
def connect():
    global count
    print(request.sid)
    users[request.sid]=count
    join_room(request.sid)
    count+=1

@socketio.on('disconnect')
def disconnect():
    leave_room(request.sid)
    print('disconnect',request.sid)

if __name__ == '__main__':
    socketio.run(app,debug=True)