import asyncio
import random
import time

async def newsProducer(myQueue):
    while True:
        await asyncio.sleep(1)
        print('Putting news item onto queue')
        await myQueue.put(random.randint(1,5))

async def newsConsumer(id,myQueue):
    print(myQueue)
    while True:
        print('Consumer: {} attempting to get from queue'.format(id))
        item=await myQueue.get()
        if item is None:
            break
        print('Consumer: {} consumed article with id: {}'.format(id,item))

def doWork():
    loop=asyncio.get_event_loop()
    myQueue=asyncio.Queue(loop=loop,maxsize=10)
    try:
        loop.run_until_complete(asyncio.gather(newsProducer(myQueue), newsConsumer(1, myQueue), newsConsumer(2, myQueue)))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

if __name__=="__main__":
    doWork()