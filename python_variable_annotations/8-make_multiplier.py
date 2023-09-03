#!/usr/bin/env python3
"""annotated function make_multiplier"""

from typing import Callable, Iterator, Union, Optional


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiply(x: float) -> float:
        """multiplies a float by multiplier"""
    return (x * multiplier)
return multiply
