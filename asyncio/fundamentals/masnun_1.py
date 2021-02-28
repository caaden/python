from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
def return_after_5_secs(message):
    sleep(5)
    return message
 
pool = ThreadPoolExecutor(1)
 
# submit the blocking process to the pool
future = pool.submit(return_after_5_secs, ("hello"))
# check to see if process is complete
print(future.done())
# wait 5 s
sleep(5)
print(future.done())
print(future.result())