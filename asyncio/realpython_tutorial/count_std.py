import asyncio
import time

def count():
    print ('one')
    time.sleep(1)
    print('two')

def main():
    count()
    count()
    count()


if __name__=="__main__":
    
    s=time.perf_counter()
    # Run main. /
    # Each instance of count will print(one), then communicate to the event loop that it is taking a 1s break.  The next loop is given control.
    main()
    elapsed=time.perf_counter()-s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')