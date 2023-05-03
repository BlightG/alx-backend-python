#!/usr/bin/env python3
""" a module housing the function async_generator """
import random
import asyncio


async def async_generator() -> int:
    """ a function that asyncrounously yields a random number
        betweeen 1 and 10 for 10 loops
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
