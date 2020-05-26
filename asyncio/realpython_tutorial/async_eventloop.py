import asyncio

async def hello()-> None:
    print('Hello...')
    await asyncio.sleep(3)

async def world()-> None:
    print('World!')

async def main():
    # asycio.gather forms the event loop
    await asyncio.gather(hello(),hello(),world())
    print('DONE!')
    
if __name__=='__main__':
    asyncio.run(main())