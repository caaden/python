import asyncio

# coroutine that is used in simple event loop
async def myCoroutine():
    print('My Coroutine')

# launch simple event loop
# run until completed
loop=asyncio.get_event_loop()
try:
    loop.run_until_complete(myCoroutine())
finally:
    loop.close()

