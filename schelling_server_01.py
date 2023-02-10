from flask import Flask, render_template, request
from flask_socketio import SocketIO,join_room, leave_room
from random import random
from schelling import Experiment,Agent
import json

threads = {}
users={}
count=0
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


def background_thread(user_id,data):
    setup_dict = json.loads(data)
    size = setup_dict["size"]
    density = float(setup_dict["density"])
    similar = float(setup_dict["similar"])
    experiment = Experiment(size)
    experiment.setUp(int(size*size*density),similar)
    while users[user_id]==True:
        experiment.iterate()
        sim, happy, unhappy = experiment.getResultMatrix()
        socketio.emit('data', [sim, happy, unhappy], to = user_id)
        print(user_id,sim,users[user_id])
        socketio.sleep(1)
    users.pop(user_id)

@app.route('/')
def index():
    return render_template('Shelling01.html')

@socketio.on('message')
def handle_message(data):
    users[request.sid]= True
    threads[request.sid]=socketio.start_background_task(background_thread,request.sid,data)

@socketio.on('connect')
def connect():
    join_room(request.sid)

@socketio.on('disconnect')
def disconnect():
    users[request.sid]=False
    print('disconnect',request.sid),users[request.sid]
    leave_room(request.sid)
    
    

if __name__ == '__main__':
    socketio.run(app,debug=True)