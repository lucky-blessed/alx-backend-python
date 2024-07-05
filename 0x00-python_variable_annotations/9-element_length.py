#!/usr/bin/env python3
"""
Module to return value with appropriate type
"""


from typing import Iterable, Tuple


def element_length(lst: Iterable[str]) -> list[Tuple[str, int]]:
    """
    Returns a list of tuples with each tuple containing element from lst.

    Args:
        lst (Iterable[str]): An iterable containing strings.

    Returns:
        list[Tuple[str, int]]: Tuple list with first elem a str from lst
    """
    return [(i, len(i)) for i in lst]
