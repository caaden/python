import asyncio

async def myCoroutine(): 
    print('Start Work')
    # cede controll back to event loop to do something else
    # no other coroutines defined in this program, so will do nothing.
    await asyncio.sleep(5)
    print('End Work')

def main():
    # create a new event loop
    loop=asyncio.get_event_loop()

    #launch the event loop
    try:
        loop.run_until_complete(myCoroutine())
    finally:
        loop.close()

if __name__== "__main__":
    main()