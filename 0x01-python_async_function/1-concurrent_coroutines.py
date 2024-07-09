#!/usr/bin/env python3
"""
1-concurrent_coroutines module
"""


import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with specified max_delay
    and return list of all delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random call.

        Returns:
            List[float]: List of delays in ascending order.
        """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
