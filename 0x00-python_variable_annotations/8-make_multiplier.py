#!/usr/bin/env python3
"""
Module to creat a multiplier function
"""


from typing import callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        callable[[float], float]: Function to multiply a float by a multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
