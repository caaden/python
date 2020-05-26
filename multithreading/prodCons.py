from threading import Thread
from queue import Queue

q = Queue()
final_results = []

def producer():
    for i in range(100):
        q.put(i)
        

def consumer():
    while True:
        number = q.get()
        result = (number, number**2)
        final_results.append(result)
        q.task_done()
   
   
for i in range(5):
    t = Thread(target=consumer)
    t.daemon = True
    t.start()
    
producer()

q.join()

print(final_results)