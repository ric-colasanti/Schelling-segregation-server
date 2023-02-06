from flask import Flask,render_template
from flask_sock import Sock
import time

sock = Sock()
app = Flask(__name__)
sock.init_app(app)

@app.route('/')
def index():
    print("here")
    return render_template('Echo1.html')


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        for i in range(10):
            sock.send(data)
            time.sleep(0.5)            
        
if __name__ == '__main__':
  app.run(debug=True)