async def mygen(u: int=10):
    # returns i, then waits 
    i=0
    while i<u:
        print(i)
        yield 2**i
        i+=1
        await asyncio.sleep(0.5)

async def main():
    # THIS DOES NOT ENABLE concurrent generation. g is formed first, then f.
    # call mygen to generate list g, pass control to event loop when delayed
    print('Go g.')
    g=[i async for i in mygen(15)]
    print('Go f.')
    # call mygen to generate list f, pass control to event loop when delayed
    # f=[i async for i in mygen()]
    f=[j async for j in mygen(10) if not (j//3%5)]
    # f,g block
    return g, f

if __name__ == '__main__':
    import asyncio
    # You can think of an event loop as something like a while True loop that monitors coroutines, 
    # taking feedback on what’s idle, and looking around for things that can be executed in the meantime. 
    # It is able to wake up an idle coroutine when whatever that coroutine is waiting on becomes available.
    g,f=asyncio.run(main())
    print(g)
    print(f)