import asyncio
import time

async def waiter(event):

    print(f"waiting for it ...{time.strftime('%X')}")
    await event.wait()
    print(f"got it at...{time.strftime('%X')}")

async def setter(event,wait_time):
    await asyncio.sleep(wait_time)
    event.set()

async def main_event():
    # Create an Event object.
    event = asyncio.Event()
    wait_time=3

    # Spawn a tasks that wait and set the event
    waiter_task = asyncio.create_task(waiter(event))
    setter_task = asyncio.create_task(setter(event,wait_time))
    futures = asyncio.gather(waiter_task,setter_task)
    await futures

asyncio.run(main_event())