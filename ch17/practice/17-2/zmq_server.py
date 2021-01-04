import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind('tcp://%s:%s' % (host, port))

print('Server started at', datetime.utcnow())
while True:
    message = server.recv()
    if message == b'time':
        now = datetime.utcnow()
        data = str(now)
        server.send(bytes(data, 'utf-8'))
        print('Server sent', data)
        