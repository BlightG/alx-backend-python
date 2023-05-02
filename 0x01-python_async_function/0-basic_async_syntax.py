#!/usr/bin/env python3
""" a midlue housing the wait_random function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait_random takes in an integer argument max_delay,
        with a default value of 10,
        it waits for a random delay between 0 and max_delay
        (included and float value) seconds and eventually returns it.
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
