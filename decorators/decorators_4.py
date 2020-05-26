#%%
import numpy as np

#%% define decorator
def smartLog(func):
    def doWork(x):
        if x<=0:
            print("Can't take log of negative number.")
            return
        else:
            return func(x)
    return doWork

@smartLog
def takeLog(x):
    logx=np.log(x)
    print('Log(x)=',str(logx))
    return logx

#%%
takeLog(10)
takeLog(-1)

#%%
