#!/usr/bin/env python3
"""Annotate the below function’s parameters and return values with the appropriate types"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples, each containing a sequence and its length"""
    return [(i, len(i)) for i in lst]   
