import zmq
import sys
import time

port1='5556'
# provide two ports of two different servers to connect to simultaneously
if len(sys.argv)>1:
    port1=sys.argv[1]
    int(port1)

if len(sys.argv)>2:
    port2=sys.argv[2]
    int(port2)

context=zmq.Context()
print('Connecting to server...')
socket=context.socket(zmq.REQ)
# notice client socket can connect to two different servers
socket.connect(f'tcp://localhost:{str(port1)}')
if len(sys.argv)>2:
    socket.connect(f'tcp://localhost:{str(port2)}')


for request in range(1,10):
    # requests alternate between port1 and port2 sockets
    print(f'Sending request {request}...')
    socket.send(b'Hello')
    # can NOT send another request until response is received
    message=socket.recv().decode('UTF-8')
    print(f'Received reply {request} [{message}] ')
    time.sleep(1)