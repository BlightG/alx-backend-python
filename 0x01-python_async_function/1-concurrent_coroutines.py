#!/usr/bin/env python3
''' a modlue housing the wait_n async function '''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    '''
        a function that runs wait_random n times and return list of wait times
    '''
    task = []
    for i in range(n):
        task.append(wait_random(max_delay))
    
    task_times = []
    for time  in asyncio.as_completed(task):
        task_times.append(await time)
    return task_times
