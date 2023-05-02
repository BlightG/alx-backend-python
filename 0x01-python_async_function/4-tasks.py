#!/usr/bin/env python3
""" a module for the function task_wait_n """
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> float:
    '''
        a function that runs wait_random n times and return list of times
    '''
    return await asyncio.gather(*(task_wait_random(max_delay)
                                  for i in range(n)))
