#!/usr/bin/env python3
"""
Task wait random module
"""
import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine
    with the specific max_delay

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        Asyncio.Task: Created task.
    """
    return asyncio.create_task(wait_random(max_delay))
