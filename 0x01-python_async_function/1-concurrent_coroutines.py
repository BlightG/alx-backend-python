#!/usr/bin/env python3
''' a modlue housing the wait_n async function '''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
        a function that runs wait_random n times and return list of wait times
    '''
    task = [i async for i in async_generator()]
    return task
