#%% Modules
import numpy as np
import time
import warnings
import threading
import queue


#Disable warnings
warnings.filterwarnings("ignore")
BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

#consumer thread = predictor/inference code
class consumer():
    def __init__(self):
        #constructor creates new thread
        self.Go=True

    def run(self):
        while self.Go==True:
            if not q.empty():
                datafile=q.get()
                predModel(datafile)
        return

def predModel(datafileID):
    delay=2
    print('Start predicting model: ',datafileID)
    time.sleep(delay)
    print('Done predicting')
    print('Processing time: ',delay)

#producer thread = gocator controller
class producer():
    def __init__(self,consumer):
        self.vG=simulate_Gocator()
        self.Go=True
        self.cN=consumer
        self.t=time.time()
    def run(self):
        while self.Go==True:
            #add new data file to the queue
            if not q.full():
               self.vG.getData()
               print('Time between samples: ',time.time()-self.t)
               self.t=time.time()
               q.put(self.vG.meas)
               if self.vG.meas==0:
                   self.Go=False
                   self.cN.Go=False #quit consumer thread if producer stops
        return 


class simulate_Gocator(object):
    def __init__(self):
        #10 measurement buffer... in reality, the gocator will run until timeout 
        self.mvec=[1,2,3,4,5,6,7,8,9,0]
        self.mctr=0
        self.meas=None
        self.start=0
        self.end=None
        self.delay=4
    def getData(self):
        print('Getting data from Gocator')
        time.sleep(self.delay)
        self.meas=self.mvec[self.mctr]
        print('Got new Data: ',self.meas)
        self.mctr+=1

if __name__ == "__main__":
    c=consumer()
    p=producer(c)
    ct = threading.Thread(target=c.run)
    pt = threading.Thread(target=p.run)
    ct.start()
    pt.start()
    pt.join()
    ct.join()
            