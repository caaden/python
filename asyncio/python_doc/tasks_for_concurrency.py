import asyncio
import time

async def say_after(delay, what):
    # sample coroutine
    await asyncio.sleep(delay)
    print(what)

def say_after_blk(delay, what):
    # sample blocking subroutine
    time.sleep(delay)
    print(what)

async def main():
    # takes three seconds to complete because coroutines are not added to event loop as tasks
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")

async def main_task():
    # takes two seconds because we create and add tasks to the event loop for concurrency
    task1 = asyncio.create_task(say_after(1,'you'))
    task2 = asyncio.create_task(say_after(2,'suck'))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"stopped at {time.strftime('%X')}")

async def main_gather():
    # alternatively, can use gather to run coroutines currently
    coroutine1 = say_after(1,'but getting ')
    coroutine2 = say_after(2,'better')
    print(f"started at {time.strftime('%X')}")
    await asyncio.gather(coroutine1,coroutine2)
    print(f"stopped at {time.strftime('%X')}")

async def main_sleep():
    # can also use asyncio.sleep to suspend main and execute other events in the event loop
    coroutine1 = say_after(1,'and better ')
    coroutine2 = say_after(2,'and even better')
    print(f"started at {time.strftime('%X')}")
    futures = asyncio.gather(coroutine1,coroutine2)
    # time = 1.5 will allow coroutine1 to run, but not coroutine2 because it times out
    # time = 2.2 will let both run
    await asyncio.sleep(2.2)
    print(f"stopped at {time.strftime('%X')}")

async def main_runblockingcode():
    # alternatively, can run blocking code in new threads (or processes) using the same event loop
    loop=asyncio.get_running_loop()
    print(f"started at {time.strftime('%X')}")
    # default conncurrency is multithreading, can also specify multiprocess
    future_1=loop.run_in_executor(None,say_after_blk,1,'over ')
    future_2=loop.run_in_executor(None,say_after_blk,2,'time ')
    await asyncio.gather(future_1,future_2)
    print(f"stopped at {time.strftime('%X')}")
    

print('---')
asyncio.run(main())
print('---')
asyncio.run(main_task())
print('---')
asyncio.run(main_gather())
print('---')
asyncio.run(main_sleep())
print('---')
asyncio.run(main_runblockingcode())

