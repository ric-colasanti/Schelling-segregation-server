import eventlet
from eventlet import wsgi
from schelling_server_01 import create_app

app  = create_app()
http_server = wsgi.server(eventlet.listen(('0.0.0.0', 5000)),app)
http_server.serve_forever()
