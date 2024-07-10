#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""


import asyncio
import time
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in
    parallel using asyncio.gather. Measures the total runtime
    and returns it.
    """
    start_time = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = time.perf_counter()
    return end_time - start_time
