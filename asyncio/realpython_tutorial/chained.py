import asyncio
import random
import time

async def part1(n: int) -> str:
    #input: n (integer)
    #output a string

    #draw delay from 0-10
    i=random.randint(0,10)
    # sleep for delay
    print(f'part1({n}) sleeping for {i} seconds.')
    # pass control back to chain
    await asyncio.sleep(i)
    result=f'result{n}-1'
    print(f'Returning part1({n})=={result}.')
    return result

async def part2(n: int, arg: str) -> str:
    #input: n (integer)
    #       arg (string)
    #output a string
    # draw a delay from 0-10
    i=random.randint(0,10)
    # sleep for delay, report part1 connection
    print(f'part2({n,arg}) sleeping for {i} seconds.')
    # pass controll back to chain
    await asyncio.sleep(i)
    result=f'result{n}-2 derived from {arg}'
    print(f'Returning part1({n, arg})=={result}.')
    return result

async def chain(n:int) -> None:
    start=time.perf_counter()
    # call part1 coroutine for each n.
    p1=await part1(n)
    # items are chained, while part1 is delayed, move on to part2 - with handle to p1 so availability of p1 blocks.
    p2=await part2(n,p1)
    # availability of p2 blocks
    end = time.perf_counter()-start
    print(f'--> Chained result{n} => {p2} (took {end:0.2f} seconds).')

async def main(*args):
    # gathers chain coroutines and waits for completion (like join)
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    import sys
    random.seed(444)
    args=[1,2,3] if len(sys.argv) == 1 else map(int,sys.argv[1:])
    start=time.perf_counter()
    # default pass in [1,2,3]
    asyncio.run(main(*args)) # *args unpacks input iterable or list
    end=time.perf_counter()-start
    print(f'Program finished in {end:0.2f} seconds')

