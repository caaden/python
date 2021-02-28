# Launches 6 blocking tasks using 3 processes. 
# The first three processors run the first three blocking tasks.  
# They return to the process pool when the work is done to pick up another task. 

# OUTPUT:
# PID 18014 run_blocking_tasks: starting
# PID 18014 run_blocking_tasks: creating executor tasks
# PID 18014 run_blocking_tasks: waiting for executor tasks
# PID 18015          blocks(0): running
# PID 18016          blocks(1): running
# PID 18017          blocks(2): running
# PID 18017          blocks(2): done
# PID 18017          blocks(3): running
# PID 18016          blocks(1): done
# PID 18015          blocks(0): done
# PID 18016          blocks(4): running
# PID 18015          blocks(5): running
# PID 18017          blocks(3): done
# PID 18015          blocks(5): done
# PID 18016          blocks(4): done
# PID 18014 run_blocking_tasks: results: [9, 0, 16, 25, 1, 4]
# PID 18014 run_blocking_tasks: exiting

import asyncio
import concurrent.futures
# The concurrent.futures module provides a high-level interface for asynchronously executing callables.
# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. 
# Both implement the same interface, which is defined by the abstract Executor class.
import logging
import sys
import time

def blocks(n):
    # initialize a new logger for <blocks>
    log=logging.getLogger(blocks.__name__+f'({n})')
    log.info('running')
    # launch a blocking process
    time.sleep(5)
    log.info('done')
    return n**2

async def run_blocking_tasks(executor):
    # initialize a new logger for <run_blocking_tasks>
    log=logging.getLogger(run_blocking_tasks.__name__)
    log.info('starting')
    log.info('creating executor tasks')
    # initialize event loop
    loop=asyncio.get_event_loop()
    # run consecutive asynchronous blocking tasks using a comprehension.  The comprehension itself is non-blocking.
    blocking_tasks=[
        # creates 6 blocking futures:
        # run_in_executor method takes an executor instance, in this case (concurrent.futures.ThreadPoolExecutor with 3 workers) 
        # a coroutine (in this case blocks), and arguments.
        # returns a Future (an eventual result of an asyncronous operation)
        loop.run_in_executor(executor,blocks,i) for i in range(6)
    ]

    log.info('waiting for executor tasks')
    # asyncio.wait blocks until tasks are complete
    completed,pending=await asyncio.wait(blocking_tasks,return_when='ALL_COMPLETED')
    results=[t.result() for t in completed]
    log.info(f'results: {results}')
    log.info('exiting')

if __name__=='__main__':
    # configure loggint to show thread name and where log message originates
    logging.basicConfig(
        level=logging.INFO,
        format='PID %(process)5s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    # Create a limited threadpool
    executor=concurrent.futures.ProcessPoolExecutor(
        max_workers=3,
    )
    # initialize the event loop for concurrent exectution of blocking tasks
    event_loop=asyncio.get_event_loop()
    try:
        # run blocking tasks
        event_loop.run_until_complete(run_blocking_tasks(executor))
    finally:
        event_loop.close()