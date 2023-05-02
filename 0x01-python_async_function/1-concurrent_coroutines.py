#!/usr/bin/env python3
""" a modlue housing the wait_n async function """
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ a function that runs wait_random n times
        and return list of wait times
    """
    time = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return time
