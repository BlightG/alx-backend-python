#!/usr/bin/env python3
""" a module for the function task_wait_n """
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> float:
    """ new aawit function """
    return await asyncio.gather(*(task_wait_random(max_delay)
                                  for i in range(n)))
