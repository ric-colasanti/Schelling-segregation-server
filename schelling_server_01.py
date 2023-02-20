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

def create_app():
     print('running***')
     return socketio.run(app)

def background_thread(user_id,data):
    setup_dict = json.loads(data)
    size = setup_dict["size"]
    density = float(setup_dict["density"])
    likeness = float(setup_dict["likeness"])
    users[user_id]["experiment"].setUp(int(size*size*density),likeness)
    while users[user_id]["run"]!="end":  ## remember to use user_id here cant do request
        if users[user_id]["run"]=="run":
            users[user_id]["experiment"].iterate()
            sim, happy, unhappy = users[user_id]["experiment"].getResultMatrix()
            socketio.emit('data', [sim, happy, unhappy], to = user_id)
        socketio.sleep(0.5)
    if users[user_id]["run"]=="end":
        users.pop(user_id)

@app.route('/')
def index():
    print("here")
    return render_template('index.html')


@app.route('/Shelling')
def Shelling():
    return render_template('Shelling01.html')

@socketio.on('message')
def handle_message(data):
    threads[request.sid]=socketio.start_background_task(background_thread,request.sid,data)

@socketio.on('stop')
def handel_stop():
    users[request.sid]["run"]="stop"

@socketio.on('restart')
def handel_restart():
    print("restart")
    users[request.sid]["run"]="run"
    

@socketio.on('reset')
def handel_reset(data):
    print("reset")
    user_id = request.sid 
    users[user_id]["experiment"] = Experiment(40)
    setup_dict = json.loads(data)
    size = setup_dict["size"]
    density = float(setup_dict["density"])
    likeness = float(setup_dict["likeness"])
    users[user_id]["experiment"].setUp(int(size*size*density),likeness)
    users[user_id]["run"]="run"    

@socketio.on('connect')
def connect():
    print('connect')
    user_id = request.sid 
    users[user_id]={}
    users[user_id]["run"]= "run"
    users[user_id]["experiment"] = Experiment(40)
    join_room(user_id)
    happy = users[user_id]["experiment"].getMatrix()
    socketio.emit('data', [happy, 0,0], to = user_id)

@socketio.on('disconnect')
def disconnect():
    users[request.sid]["run"]="end"
    leave_room(request.sid)
    
    
if __name__ == '__main__':
    socketio.run(app,debug=True,host="127.0.0.1")
