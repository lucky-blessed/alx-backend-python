from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Args:
       lst (Sequence): Sequence (list, tuple, etc.) elements of any type.

       Returns:
           Union[Any, None]: Element of sequence, or None if sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
