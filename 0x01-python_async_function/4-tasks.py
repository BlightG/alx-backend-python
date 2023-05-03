#!/usr/bin/env python3
""" a module for the function task_wait_n """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) List[float]:
    """ new aawit function """

    task = []
    for i in range(n):
        task.append(task_wait_random(max_delay))

    task_times = []
    for time in asyncio.as_completed(task):
        task_times.append(await time)
    return task_times
