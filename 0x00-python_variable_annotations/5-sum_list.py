#!/usr/bin/env python3
"""
Module to sum a list of floats
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)
