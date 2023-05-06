#!/usr/bin/env python3
""" a mdule with the function async_generator """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ return a list of async results """
    task = [i async for i in async_generator()]
    return task
