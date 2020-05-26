import asyncio

async def myCoroutine():
    while True:
        await asyncio.sleep(1)
        print('task executed')
        
def main():
    loop=asyncio.get_event_loop()
    try:
        asyncio.ensure_future(myCoroutine())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("closing loop")
        loop.close()

if __name__== "__main__":
    main()