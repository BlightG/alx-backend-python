#!/usr/bin/env python3
""" a module housing the function async_generator """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ a function that asyncrounously yields a random number
        betweeen 1 and 10 for 10 loops
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
