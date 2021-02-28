https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html

Publishers: senders of messages
Subscribers: receivers of messages

Messages are published without knowledge of what/if/howmany subscribers of the information exists

Setting up a publisher:
-create a context
-define a new socket
-bind the socket to an endpoint
-create a message including a topic and payload
-serialize the message

Scenario 1: single Subscriber, multiple publishers
    -subscriber connects to multiple publishers
    -messages from publishers are interleaved

Scenario 2: multiple subscribers, single publisher

Data is published along with a topic.  Subscriber filters/selects on topics.

python3 pub_server.py 5556
python3 pub_server.py 5546
python3 sub_client.py 5556 5546