import asyncio
import itertools as it 
import os
import random
import time

async def makeitem(size: int=5)->str:
    return os.urandom(size).hex()

async def randsleep(a: int=1, b: int=5, caller=None)-> None:
    # draw delay from 0-10
    i=random.randint(0,10)
    if caller: 
        print(f'{caller} sleeping for {i} seconds.')
    # pass controll back to produce event loop
    await asyncio.sleep(i)

async def produce(name: int, q: asyncio.Queue) -> None:
    # draw from 0-10
    n=random.randint(0,10)
    # iterator generates n dummy vars from draw
    for _ in it.repeat(None,n):
        # put producer to sleep, pass control back to main event loop
        await randsleep(caller=f'Producer {name}')
        # make an item, pass control back to main event loop
        # i=... is blocking
        i=await makeitem()
        t=time.perf_counter()
        # put item in queue with timestamp, pass control back to main event loop
        await q.put((i,t))
        print(f'Producer {name} added <{i}> to queue')

async def consume(name: int, q:asyncio.Queue) -> None:
    while True:
        # put consumer to sleep, pass control back to main event loop
        await randsleep(caller=f'Consumer {name}')
        # pop item off the queue, pass control back to main event loop
        i,t=await q.get()
        now=time.perf_counter()
        print(f'Consumer {name} got element <{i}> in {now-t:0.5f} seconds.')
        # declare the job is done
        q.task_done()
        
async def main(nprod: int, ncon: int):
    q=asyncio.Queue()
    # spawn nprod producers, each calling produce with queue
    producers=[asyncio.create_task(produce(n,q)) for n in range(nprod)]
    # spawn consumers
    consumers=[asyncio.create_task(consume(n,q)) for n in range(ncon)]
    # add all producers to the event loop
    await asyncio.gather(*producers)
    # await q.join() #implicitly await consumers too
    # for c in consumers: #dismiss consumers when job is done
    #     c.cancel() 

if __name__=="__main__":
    import argparse
    random.seed(444)
    parser=argparse.ArgumentParser()
    parser.add_argument('-p','--nprod',type=int,default=5)
    parser.add_argument('-c','--ncon',type=int,default=5)
    ns=vars(parser.parse_args())
    start=time.perf_counter()
    # uses asyncio.run to initiate the main event loop
    asyncio.run(main(ns['nprod'],ns['ncon']))
    elapsed=time.perf_counter()-start
    print(f'Program completed in {elapsed:0.5f} seconds.')