import sys
import zmq

port1 ='5556'
if len(sys.argv)>1:
    port1=sys.argv[1]
    int(port1)
if len(sys.argv)>2:
    port2=sys.argv[2]
    int(port2)

#create zmq context manager
context=zmq.Context()
#define subsriber socket 
socket=context.socket(zmq.SUB)

print('Collecting updates from weather server...')
# connect socket to publisher endpoints
socket.connect(f'tcp://localhost:{port1}')
if len(sys.argv)>2:
    socket.connect(f'tcp://localhost:{port2}')


#Set socket options, Subscribe to zip-code, default is 02128 = East Boston
topicfilter=b"2128"
socket.setsockopt(zmq.SUBSCRIBE,topicfilter)

total_value=0
for update_nbr in range(5):
    string=socket.recv()
    topic,messagedata=string.split()
    topic=topic.decode('UTF-8')
    messagedata=messagedata.decode('UTF-8')
    total_value+=int(messagedata)
    print(f'{topic},{messagedata}')

print(f'Average messagedata value for topic {topic} was {total_value/update_nbr}')


