#!/usr/bin/env python3
"""
0-basic_async_syntax module
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait a random delay between 0 and max_delay seconds and return the delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 0.

    Returns:
        float: The actual delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
