# Schelling-segregation-server
A python version of Schelling's segregation model run within a flask server with two way interaction with  WebSockets

### pip requirements
run pip install -r requirements.txt

flask
flask-sock
flask_socketio

### schelling_server_01.py
This is the flask server that uses flask_socketio to push data to a html js page that displays the output of the model

### schelling.py
This is the schelling segregation model written in python

Directory layout

static

    css
    js
templates
    
    index.html    



