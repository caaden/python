import zmq
import time
import sys

# initialize server port
port = '5556'
# provide port as input arg
if len(sys.argv)>1:
    port=sys.argv[1]
    int(port)

# create socket of type REP, which means it will 
# block on recv() unless it has recieved a request
context=zmq.Context()
socket=context.socket(zmq.REP)
socket.bind(f'tcp://*:{port}')

while True:
    # Wait for next request from client
    message=socket.recv().decode('UTF-8')
    print(f'Received request: {message}')
    time.sleep(2)
    payload=f'World from {port}'
    socket.send(payload.encode('UTF-8'))