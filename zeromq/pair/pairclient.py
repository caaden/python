import zmq
import random
import sys
import time

port='5556'
context=zmq.Context()
socket=context.socket(zmq.PAIR)
# connect to server
socket.connect(f'tcp://localhost:{port}')

while True:
    # get messages from server
    msg=socket.recv().decode('UTF-8')
    print(msg)
    socket.send(b'client message to server1')
    socket.send(b'client message to server2')
    time.sleep(1)