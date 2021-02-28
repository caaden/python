import asyncio

# The syntax async def introduces either a native coroutine or an asynchronous generator. 
# await: passes control back to event loop, suspends operation of surrounding coroutine
# can only use await inside an async def function

async def count():
    print ('one')
    # await passes control back to event loop and suspends the operation of the surrounding coroutine
    # asyncio.sleep() is a stand-in for a non-blocking real process 
    # will suspend current count, pass controll back to main.  Then return to count() after wait.  
    # note: sleep.time() is blocking
    await asyncio.sleep(1)
    print('two')

async def calling_function():
    # event loop
    event_loop=asyncio.gather(count(), count(), count())
    await event_loop

if __name__=="__main__":
    import time
    s=time.perf_counter()
    # Run main. /
    # Each instance of count will print(one), then communicate to the event loop that it is taking a 1s break.  The next loop is given control.
    asyncio.run(calling_function())
    elapsed=time.perf_counter()-s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')