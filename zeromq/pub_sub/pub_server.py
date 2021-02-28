import zmq
import random
import sys
import time

port='5556'
if len(sys.argv)>1:
    port=sys.argv[1]
    int(port)

# create zmq context manager
context=zmq.Context()

#define up a publisher socket
socket=context.socket(zmq.PUB)
#bind socket to endpoint
socket.bind(f'tcp://*:{port}')

while True:
    # random zip-code topic
    topic=random.randrange(2120,2130)
    messagedata=random.randrange(1,215)-80
    print(f'topic, messagedata = {topic},{messagedata}')
    #serialize message
    msg=f'{topic} {messagedata}'.encode('UTF-8')
    #send
    socket.send(msg)
    time.sleep(1)
