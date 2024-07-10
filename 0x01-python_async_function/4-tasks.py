#!/usr/bin/env python3
"""
Module that uses task_wait_n instead of task_wait_random
"""


import asyncio
from typing import List
from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay
    and return list of all delays in ascending

    Args:
        n (int): Number of times to spawn the task_wait_random call.


    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
