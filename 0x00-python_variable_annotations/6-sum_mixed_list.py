#!/usr/bin/python3
"""
Module to sum a mixed list of integers and float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the list of integers and flaots.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers and float to sum.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
