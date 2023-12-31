#!/usr/bin/env python3
"""
Run file 0-main.py as an example for the call
Type ./0-main.py at your console
The result should be:
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    __Holberton Instructions__
    Function named index_range that takes two integer
    arguments page and page_size
    The function returns a tuple of size two, containing
    a start index and an end index corresponding to the
    range of indexes to return in a list
    for those particular pagination parameters
    Page numbers are 1-indexed i.e the first page is 1
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
