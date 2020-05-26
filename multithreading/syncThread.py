import threading
import time

exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        #constructor creates new thread
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        #run method is entry point for thread 
        print('starting '+self.name)
        #get lock to synch threads
        threadLock.acquire()
        #each new thread will call print time 5 times, then exit 
        print_time(self.name,self.counter,5)
        # Free lock to release next thread
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter: 
        if exitFlag: #not sure why this is used- doesn't do anything
            threadName.exit()
        time.sleep(delay) #report the time after delay
        print("%s: %s" % (threadName,time.ctime(time.time())))
        counter -=1

threadLock = threading.Lock()
#create thread list
threads=[]

thread1=myThread(1,"Thread-1",1) #create new threads
thread2=myThread(2,"Thread-2",2)

thread1.start() #starts thread by calling run method
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")