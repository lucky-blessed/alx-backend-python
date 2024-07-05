#!/usr/bin/env python3
"""
Module for converting a string and int/float to a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a dtring and square of an int of float.

    Args:
        k (str): The string to be included in the tuple.
        v (Union[int, float]): The int or float to square inthe tuple.

    Returns:
        Tuple[str, float]: Tuple with the string and square of int or float.
    """
    return (k, float(v ** 2))
