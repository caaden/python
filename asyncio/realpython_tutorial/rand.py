import asyncio
import random

#ansi colors
c=(
    '\033[0m', #end of color
    '\033[36m', # cyan
    '\033[91m', # red
    '\033[35m', # magenta
)

# primary coroutine
async def makerandom(idx: int, threshold: int=6) -> int:     # -> defines return type
    # Inputs: 
    # idx: process index
    # threshold: target 

    print(c[idx+1] + f'initiated makerandom({idx}).')
    # draw i
    i=random.randint(0,10)
    # test i < threshold, if too low then draw again
    while i<=threshold:
        # report failed test
        print(c[idx+1] + f'makerandom({idx}) == {i} too low; retrying.')
        # return controll to event loop, sleep time depends on process index
        await asyncio.sleep(idx+1)
        i=random.randint(0,10)
    # report number exceeding threshold
    print(c[idx+1] + f'---> Finished: makerandom({idx})=={i}' + c[0])
    return i

async def main():
    # event loop starts 3 new coroutines, and waits for them to finish
    # main awaits on "gather"
    res = await asyncio.gather(*(makerandom(i,10-i-1) for i in range(3)))
    return res

if __name__=="__main__":
    random.seed(444)
    r1,r2,r3 = asyncio.run(main())
    print()
    print(f'r1: {r1}, r2: {r2}, r3: {r3}')