import asyncio
import time

async def myWorker(lock,i):
    print(f'worker {i} attempting to attain lock')
    with await lock:
        print(f'currently locked by worker {i}')
        time.sleep(2)
    print(f'worker {i} unlocked critical section') 


async def workerPool():
    lock=asyncio.Lock()
    await asyncio.wait([
        myWorker(lock,i) for i in range(3)
    ])

if __name__=="__main__":
    lock=asyncio.Lock()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(workerPool())
    print('all tasks completed')
    loop.close()