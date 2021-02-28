import asyncio
import time

async def firstWorker():
    while True:
        await asyncio.sleep(1)
        print('First Worker Executed')

async def secondWorker():
    while True:
        await asyncio.sleep(1)
        print('Second Worker Executed')

def main_v1():
    # need to explicitly get/define-new event loop
    loop=asyncio.get_event_loop()

    try:
        # explicitly add tasks to the event loop
        loop.create_task(firstWorker())
        loop.create_task(secondWorker())
        
        # gather all tasks
        # asyncio.gather(firstWorker(),secondWorker(),loop=loop)
        
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print('Closing Loop')
        loop.close()

async def main_v2():
    try:
        # us await inside a coroutine
        # loop=asyncio.get_event_loop()
        # await asyncio.gather(firstWorker(),secondWorker(),loop=loop)

        # also works because gather will reference the loop that was initialized by the 'run' command
        await asyncio.gather(firstWorker(),secondWorker())

    except KeyboardInterrupt:
        pass
    finally:
        print('Closing Loop')

if __name__ == '__main__':
    # main_v1()
    asyncio.run(main_v1())