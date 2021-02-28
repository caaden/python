import zmq
import random
import sys
import time

port='5556'
context=zmq.Context()
socket=context.socket(zmq.PAIR)
# server listening on port:port, any ip address
socket.bind(f'tcp://*:{port}')

socket.send(b'Server initial message to client3')

while True:
    # send message to client
    socket.send(b'Server message to client3')
    # client response
    msg=socket.recv().decode('UTF-8')
    print(msg)
    time.sleep(1)