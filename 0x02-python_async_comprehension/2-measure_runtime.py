#!/usr/bin/env python3
""" a module for the function measure_runtime """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ a function to measure the time taken to run async_comprehension """
    start = time.perf_counter()
    await async_comprehension()
    total_time = time.perf_counter() - start
    return total_time
